from PySide6.QtQml import qmlRegisterType

from .grid_geometry import GridLinesGeometry, AxisLineGeometry

def register_qml_types():
    """Call this function to register Python types with the QML engine."""
    # qmlRegisterType(PythonClass, URI, VersionMajor, VersionMinor, QMLName)
    qmlRegisterType(GridLinesGeometry, "CvHelpers", 0, 1, "GridLinesGeometry")
    qmlRegisterType(AxisLineGeometry, "CvHelpers", 0, 1, "AxisLineGeometry")
