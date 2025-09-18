import cv2
import numpy as np
from PySide6.QtCore import QObject, Property, Signal, QSize, QByteArray
from PySide6.QtGui import QVector3D, QQuaternion
from PySide6.QtQuick3D import QQuick3DTextureData


class ArucoTextureData(QQuick3DTextureData):
    markerIdChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._marker_id = 0
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        self.marker_size_px = 200

    @Property(int, notify=markerIdChanged)
    def markerId(self):
        return self._marker_id

    @markerId.setter
    def markerId(self, value):
        if self._marker_id != value:
            self._marker_id = value
            self.markerIdChanged.emit()

            print(f"Generating and setting texture for marker ID: {self._marker_id}")
            img_gray = cv2.aruco.generateImageMarker(
                self.aruco_dict, self._marker_id, self.marker_size_px, borderBits=1
            )
            img_rgba = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGBA)
            texture_data = QByteArray(img_rgba.tobytes())
            self.setSize(QSize(self.marker_size_px, self.marker_size_px))
            self.setTextureData(texture_data)

    def format(self):
        return QQuick3DTextureData.Format.RGBA8

    def hasAlphaChannel(self):
        return True


class Marker(QObject):
    positionChanged = Signal()
    rotationChanged = Signal()
    sizeChanged = Signal()
    textureDataChanged = Signal()

    def __init__(self, marker_id, position, rotation, size, parent=None):
        super().__init__(parent)
        self._position = position
        self._rotation = rotation
        self._size = size
        self._texture_data = ArucoTextureData()
        self._texture_data.markerId = marker_id

    @Property(QVector3D, notify=positionChanged)
    def position(self):
        return self._position

    @Property(QQuaternion, notify=rotationChanged)
    def rotation(self):
        return self._rotation

    @Property(float, notify=sizeChanged)
    def size(self):
        return self._size

    @Property(QObject, notify=textureDataChanged)
    def textureData(self):
        return self._texture_data


class MarkerController(QObject):
    markersChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._markers = []

    @Property(list, notify=markersChanged)
    def markers(self):
        return self._markers
