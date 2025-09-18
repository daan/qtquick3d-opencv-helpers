from PySide6.QtQml import qmlRegisterType

from .grid_geometry import GridLinesGeometry, AxisLineGeometry
from .marker_classes import ArucoTextureData, Marker, MarkerController
from .frustum_geometry import FrustumGeometry

def register_qml_types():
    """Call this function to register Python types with the QML engine."""
    # qmlRegisterType(PythonClass, URI, VersionMajor, VersionMinor, QMLName)
    qmlRegisterType(GridLinesGeometry, "CvHelpers", 0, 1, "GridLinesGeometry")
    qmlRegisterType(AxisLineGeometry, "CvHelpers", 0, 1, "AxisLineGeometry")
    qmlRegisterType(ArucoTextureData, "CvHelpers", 0, 1, "ArucoTexture")
    qmlRegisterType(FrustumGeometry, "CvHelpers", 0, 1, "FrustumGeometry")


