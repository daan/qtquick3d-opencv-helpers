import QtQuick
import QtQuick.Controls
import QtQuick3D
import QtQuick3D.Helpers
import CvHelpers

Window {
    width: 1280
    height: 720
    visible: true
    title: "Minimal Camera Frustum"

    View3D {
        id: view
        anchors.fill: parent
        focus: true

        Keys.onPressed: (event) => {
            if (event.key === Qt.Key_Escape) {
                Qt.quit()
            }
        }
    
        environment: SceneEnvironment {
            backgroundMode: SceneEnvironment.Color
            clearColor: "#202020"
            antialiasingMode: SceneEnvironment.MSAA
            antialiasingQuality: SceneEnvironment.High
        }
        camera: cameraNode

        Node {
            id: cameraOrigin
                PerspectiveCamera {
                    id: cameraNode
                    position: Qt.vector3d(0, 2, 5)
                    clipFar: 100
                    clipNear: 0.1
                }
        }
        OrbitCameraController {
            camera: cameraNode
            origin: cameraOrigin
            panEnabled: true
        }
    
        DirectionalLight {
            eulerRotation.x: -45
            eulerRotation.y: -30
        }
        
        Node {
            id: sceneRoot
            Grid {
	    }
	    Frustum {}
       }
    }
}
