import QtQuick
import QtQuick3D
import QtQuick3D.Helpers


Node {
  Node {
	  id: x_axis
	  eulerRotation: Qt.vector3d(0,0,-90)

	// red

     Model {
            id: x_cylinder
            geometry: CylinderGeometry {
		    radius: 0.005
     		    length: 0.7
            }
            position: Qt.vector3d(0,0.35,0)
            materials: [
                PrincipledMaterial {
                    baseColor: "#ff0000"
                    metalness: 0.1
                    roughness: 0.9
                    emissiveFactor: Qt.vector3d(1,0,0)
                    lighting: PrincipledMaterial.NoLighting
                }
            ]
            castsShadows: true
            receivesShadows: true
     }


        Model {
            id: x_cone
	    geometry: ConeGeometry {
		length: 0.2
		bottomRadius: 0.04
		topRadius: 0
	    }

            position: Qt.vector3d(0,0.8,0)
            materials: [
                PrincipledMaterial {
                    baseColor: "#ff0000"
                    metalness: 0.1
                    roughness: 0.9
                    emissiveFactor: Qt.vector3d(1,0,0)
                    lighting: PrincipledMaterial.NoLighting
                }
            ]
            castsShadows: true
            receivesShadows: true
       } 
    }

    // green

     Model {
            id: y_cylinder
            geometry: CylinderGeometry {
		    radius: 0.005
     		    length: 0.7
            }
            position: Qt.vector3d(0,0.35,0)
            materials: [
                PrincipledMaterial {
                    baseColor: "#00ff00"
                    metalness: 0.1
                    roughness: 0.9
                    emissiveFactor: Qt.vector3d(0,1,0)
                    lighting: PrincipledMaterial.NoLighting
                }
            ]
            castsShadows: true
            receivesShadows: true
     }


        Model {
            id: y_cone
	    geometry: ConeGeometry {
		length: 0.2
		bottomRadius: 0.04
		topRadius: 0
	    }

            position: Qt.vector3d(0,0.8,0)
            materials: [
                PrincipledMaterial {
                    baseColor: "#00ff00"
                    metalness: 0.1
                    roughness: 0.9
                    emissiveFactor: Qt.vector3d(0,1,0)
                    lighting: PrincipledMaterial.NoLighting
                }
            ]
            castsShadows: true
            receivesShadows: true
    }

// blue
  Model {
	  id: z_arrow
	  eulerRotation: Qt.vector3d(90,0,0)

     Model {
            id: z_cylinder
            geometry: CylinderGeometry {
		    radius: 0.005
     		    length: 0.7
	    }
	    position: Qt.vector3d(0,0.35,0)
            materials: [
                PrincipledMaterial {
                    baseColor: "#0000ff"
                    metalness: 0.1
                    roughness: 0.9
                    emissiveFactor: Qt.vector3d(0,0,1)
                    lighting: PrincipledMaterial.NoLighting
                }
            ]
            castsShadows: true
            receivesShadows: true
     }


        Model {
            id: z_cone
	    geometry: ConeGeometry {
		length: 0.2
		bottomRadius: 0.04
		topRadius: 0
	    }
            position: Qt.vector3d(0,0.8,0)
            materials: [
                PrincipledMaterial {
                    baseColor: "#0000ff"
                    metalness: 0.1
                    roughness: 0.9
                    emissiveFactor: Qt.vector3d(0,0,1)
                    lighting: PrincipledMaterial.NoLighting
                }
            ]
            castsShadows: true
            receivesShadows: true
       }  
    }
}


