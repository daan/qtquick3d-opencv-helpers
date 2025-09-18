import QtQuick
import QtQuick3D
import QtQuick3D.Helpers
import CvHelpers

Node {
    id: root

    property real markerSize: 0.1
    property ArucoTexture textureData

    Component.onCompleted: {
        if (textureData) {
            console.log("Forcing texture update on component completion")
            textureData.update()
        }
    }

    Model {
        position: Qt.vector3d(root.markerSize / 2, 0, root.markerSize / 2)
        geometry: PlaneGeometry {
            width: root.markerSize
            height: root.markerSize
            plane: PlaneGeometry.XZ
        }
        materials: [
            PrincipledMaterial {
                baseColorMap: Texture {
                    textureData: root.textureData
                }
                lighting: "NoLighting"
            }
        ]
    }

    Model {
        position: Qt.vector3d(root.markerSize / 2, 0, root.markerSize / 2)
        eulerRotation.x: 180
        geometry: PlaneGeometry {
            width: root.markerSize
            height: root.markerSize
            plane: PlaneGeometry.XZ
        }
        materials: [
            PrincipledMaterial {
                baseColor: "grey"
                lighting: "NoLighting"
            }
        ]
    }
}
