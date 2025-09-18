import QtQuick
import QtQuick3D
import CvHelpers

Node {
    id: root

    property real fov: 60.0 // Vertical field of view in degrees
    property real aspectRatio: 16.0 / 9.0
    property real scale: 0.5 // Controls the size of the frustum visualization

    Model {
        geometry: FrustumGeometry {
            fov: root.fov
            aspectRatio: root.aspectRatio
            scale: root.scale
        }
        materials: [ PrincipledMaterial { baseColor: "yellow"; lighting: "NoLighting" } ]
    }
}
