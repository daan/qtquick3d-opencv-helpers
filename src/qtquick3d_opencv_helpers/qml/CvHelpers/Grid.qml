import QtQuick
import QtQuick3D
import CvHelpers

Node {
    id: root

    property int xLines: 5
    property int zLines: 5
    property real gridInterval: 1.0
    property color gridColor: "#333333"

    // Grey grid lines
    Model {
        geometry: GridLinesGeometry {
            xLines: root.xLines
            zLines: root.zLines
            gridInterval: root.gridInterval
        }
        materials: [ PrincipledMaterial { baseColor: root.gridColor; lighting: "NoLighting" } ]
    }

    // Positive X axis (red)
    Model {
        geometry: AxisLineGeometry {
            axis: AxisLineGeometry.XAxis
            length: root.xLines * root.gridInterval
        }
        materials: [ PrincipledMaterial { baseColor: "#FF5555"; lighting: "NoLighting" } ]
    }

    // Negative X axis (grey)
    Model {
        eulerRotation.y: 180
        geometry: AxisLineGeometry {
            axis: AxisLineGeometry.XAxis
            length: root.xLines * root.gridInterval
        }
        materials: [ PrincipledMaterial { baseColor: root.gridColor; lighting: "NoLighting" } ]
    }

    // Positive Z axis (blue)
    Model {
        geometry: AxisLineGeometry {
            axis: AxisLineGeometry.ZAxis
            length: root.zLines * root.gridInterval
        }
        materials: [ PrincipledMaterial { baseColor: "#0d60dd"; lighting: "NoLighting" } ]
    }

    // Negative Z axis (grey)
    Model {
        eulerRotation.y: 180
        geometry: AxisLineGeometry {
            axis: AxisLineGeometry.ZAxis
            length: root.zLines * root.gridInterval
        }
        materials: [ PrincipledMaterial { baseColor: root.gridColor; lighting: "NoLighting" } ]
    }
}
