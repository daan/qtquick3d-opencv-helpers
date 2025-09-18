import math

import numpy as np
from PySide6.QtCore import QByteArray, Property, Signal
from PySide6.QtGui import QVector3D
from PySide6.QtQuick3D import QQuick3DGeometry


class CameraFrustumGeometry(QQuick3DGeometry):
    fovChanged = Signal()
    aspectRatioChanged = Signal()
    scaleChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._fov = 60.0
        self._aspect_ratio = 16.0 / 9.0
        self._scale = 0.5
        self.updateData()

    @Property(float, notify=fovChanged)
    def fov(self):
        return self._fov

    @fov.setter
    def fov(self, value):
        if self._fov != value:
            self._fov = value
            self.fovChanged.emit()
            self.updateData()

    @Property(float, notify=aspectRatioChanged)
    def aspectRatio(self):
        return self._aspect_ratio

    @aspectRatio.setter
    def aspectRatio(self, value):
        if self._aspect_ratio != value:
            self._aspect_ratio = value
            self.aspectRatioChanged.emit()
            self.updateData()

    @Property(float, notify=scaleChanged)
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        if self._scale != value:
            self._scale = value
            self.scaleChanged.emit()
            self.updateData()

    def updateData(self):
        self.clear()

        fov_rad = math.radians(self._fov)
        far_h = 2 * self._scale * math.tan(fov_rad / 2)
        far_w = far_h * self._aspect_ratio

        vertices = np.array([
            # 0: origin
            0, 0, 0,
            # 1: bottom-left
            -far_w / 2, -far_h / 2, -self._scale,
            # 2: bottom-right
            far_w / 2, -far_h / 2, -self._scale,
            # 3: top-right
            far_w / 2, far_h / 2, -self._scale,
            # 4: top-left
            -far_w / 2, far_h / 2, -self._scale
        ], dtype=np.float32)

        vertex_data = QByteArray(vertices.tobytes())

        self.setVertexData(vertex_data)
        self.setStride(3 * vertices.itemsize)
        self.setBounds(QVector3D(-far_w / 2, -far_h / 2, -self._scale), QVector3D(far_w / 2, far_h / 2, 0))

        self.setPrimitiveType(QQuick3DGeometry.PrimitiveType.Lines)

        self.addAttribute(QQuick3DGeometry.Attribute.PositionSemantic,
                          0,
                          QQuick3DGeometry.Attribute.F32Type)

        indices = np.array([
            # origin to corners
            0, 1, 0, 2, 0, 3, 0, 4,
            # far plane
            1, 2, 2, 3, 3, 4, 4, 1
        ], dtype=np.uint16)

        index_data = QByteArray(indices.tobytes())
        self.setIndexData(index_data)

        self.addAttribute(QQuick3DGeometry.Attribute.IndexSemantic,
                          0,
                          QQuick3DGeometry.Attribute.U16Type)
