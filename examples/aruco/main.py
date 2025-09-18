import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication, QVector3D, QQuaternion
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType

import qtquick3d_opencv_helpers
import importlib.resources

from qtquick3d_opencv_helpers.marker_classes import Marker, MarkerController

def main():
    app = QGuiApplication(sys.argv)


    engine = QQmlApplicationEngine()

    qtquick3d_opencv_helpers.register_qml_types()

    with importlib.resources.as_file(importlib.resources.files('qtquick3d_opencv_helpers') / 'qml') as qml_path:
        engine.addImportPath(str(qml_path))



    marker_controller = MarkerController()
    engine.rootContext().setContextProperty("markerController", marker_controller)
    marker_controller._markers.append(Marker(marker_id=1, position=QVector3D(0, 0.5, 0), rotation=QQuaternion(), size=1))
    marker_controller._markers.append(
        Marker(marker_id=2, position=QVector3D(1.5, 0.5, 1.5), rotation=QQuaternion.fromEulerAngles(45, 0, 0), size=1))

    script_dir = Path(__file__).parent
    qml_file = script_dir / "main.qml"
    engine.load(QUrl.fromLocalFile(str(qml_file)))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
