from enum import IntEnum
import numpy as np
from PySide6.QtCore import QByteArray, Property, Signal, QEnum
from PySide6.QtGui import QVector3D
from PySide6.QtQuick3D import QQuick3DGeometry


class GridLinesGeometry(QQuick3DGeometry):
    xLinesChanged = Signal()
    zLinesChanged = Signal()
    gridIntervalChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._x_lines = 10
        self._z_lines = 10
        self._grid_interval = 1.0
        self.updateData()

    @Property(int, notify=xLinesChanged)
    def xLines(self):
        return self._x_lines

    @xLines.setter
    def xLines(self, value):
        if self._x_lines != value:
            self._x_lines = value
            self.xLinesChanged.emit()
            self.updateData()

    @Property(int, notify=zLinesChanged)
    def zLines(self):
        return self._z_lines

    @zLines.setter
    def zLines(self, value):
        if self._z_lines != value:
            self._z_lines = value
            self.zLinesChanged.emit()
            self.updateData()

    @Property(float, notify=gridIntervalChanged)
    def gridInterval(self):
        return self._grid_interval

    @gridInterval.setter
    def gridInterval(self, value):
        if self._grid_interval != value:
            self._grid_interval = value
            self.gridIntervalChanged.emit()
            self.updateData()

    def updateData(self):
        self.clear()
        
        vertices = []
        
        x_extent = self._x_lines * self._grid_interval
        z_extent = self._z_lines * self._grid_interval
        
        # Lines parallel to Z axis
        for i in range(-self._x_lines, self._x_lines + 1):
            if i == 0: continue
            x = i * self._grid_interval
            vertices.extend([x, 0, -z_extent, x, 0, z_extent])

        # Lines parallel to X axis
        for i in range(-self._z_lines, self._z_lines + 1):
            if i == 0: continue
            z = i * self._grid_interval
            vertices.extend([-x_extent, 0, z, x_extent, 0, z])
            
        if not vertices:
            self.setBounds(QVector3D(0,0,0), QVector3D(0,0,0))
            return
            
        vertices = np.array(vertices, dtype=np.float32)
        indices = np.arange(len(vertices) // 3, dtype=np.uint32)

        vertex_data = QByteArray(vertices.tobytes())
        self.setVertexData(vertex_data)
        self.setStride(3 * vertices.itemsize)
        self.setBounds(QVector3D(-x_extent, 0, -z_extent), QVector3D(x_extent, 0, z_extent))

        self.setPrimitiveType(QQuick3DGeometry.PrimitiveType.Lines)

        self.addAttribute(QQuick3DGeometry.Attribute.PositionSemantic,
                          0,
                          QQuick3DGeometry.Attribute.F32Type)

        index_data = QByteArray(indices.tobytes())
        self.setIndexData(index_data)

        self.addAttribute(QQuick3DGeometry.Attribute.IndexSemantic,
                          0,
                          QQuick3DGeometry.Attribute.U32Type)


class AxisLineGeometry(QQuick3DGeometry):
    class Axis(IntEnum):
        XAxis = 0
        YAxis = 1
        ZAxis = 2
    QEnum(Axis)

    axisChanged = Signal()
    lengthChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._axis = AxisLineGeometry.Axis.XAxis
        self._length = 20.0
        self.updateData()

    @Property(int, notify=axisChanged)
    def axis(self):
        return self._axis

    @axis.setter
    def axis(self, value):
        if self._axis != value:
            self._axis = value
            self.axisChanged.emit()
            self.updateData()

    @Property(float, notify=lengthChanged)
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if self._length != value:
            self._length = value
            self.lengthChanged.emit()
            self.updateData()

    def updateData(self):
        self.clear()
        
        if self._axis == self.Axis.XAxis:
            vertices = np.array([0, 0, 0, self._length, 0, 0], dtype=np.float32)
            bounds_min = QVector3D(0, 0, 0)
            bounds_max = QVector3D(self._length, 0, 0)
        elif self._axis == self.Axis.YAxis:
            vertices = np.array([0, 0, 0, 0, self._length, 0], dtype=np.float32)
            bounds_min = QVector3D(0, 0, 0)
            bounds_max = QVector3D(0, self._length, 0)
        elif self._axis == self.Axis.ZAxis:
            vertices = np.array([0, 0, 0, 0, 0, self._length], dtype=np.float32)
            bounds_min = QVector3D(0, 0, 0)
            bounds_max = QVector3D(0, 0, self._length)
        else:
            vertices = np.array([], dtype=np.float32)
            bounds_min = QVector3D(0,0,0)
            bounds_max = QVector3D(0,0,0)

        indices = np.array([0, 1], dtype=np.uint16)
        
        vertex_data = QByteArray(vertices.tobytes())
        self.setVertexData(vertex_data)
        self.setStride(3 * vertices.itemsize)
        self.setBounds(bounds_min, bounds_max)

        self.setPrimitiveType(QQuick3DGeometry.PrimitiveType.Lines)

        self.addAttribute(QQuick3DGeometry.Attribute.PositionSemantic,
                          0,
                          QQuick3DGeometry.Attribute.F32Type)

        index_data = QByteArray(indices.tobytes())
        self.setIndexData(index_data)

        self.addAttribute(QQuick3DGeometry.Attribute.IndexSemantic,
                          0,
                          QQuick3DGeometry.Attribute.U16Type)
