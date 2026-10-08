from dataclasses import dataclass

@dataclass
class drone:
    part: str
    part_weight: float # in kg
    #pos
    x: float
    y: float
    z: float


topLeftProp = drone("top leftpropeller", 0.5, -10.0, 20.0, 30.0)
topRightProp = drone("top right propeller", 0.5, 10.0, 20.0, 30.0)
bottomLeftProp = drone("bottom left propeller", 0.5, -10.0, -20.0, 30.0)
bottomRightProp = drone("bottom right propeller", 0.5, 10.0, -20.0, 30.0)

center_topLeftProp = (topLeftProp.x * topLeftProp.part_weight,
               topLeftProp.y * topLeftProp.part_weight,
                topLeftProp.z * topLeftProp.part_weight)

center_topRightProp = (topRightProp.x * topRightProp.part_weight,
                topRightProp.y * topRightProp.part_weight,
                 topRightProp.z * topRightProp.part_weight)

center_bottomLeftProp = (bottomLeftProp.x * bottomLeftProp.part_weight,
                   bottomLeftProp.y * bottomLeftProp.part_weight,
                    bottomLeftProp.z * bottomLeftProp.part_weight)

center_bottomRightProp = (bottomRightProp.x * bottomRightProp.part_weight,
                    bottomRightProp.y * bottomRightProp.part_weight,
                     bottomRightProp.z * bottomRightProp.part_weight)

center_grav = (center_topLeftProp[0] + center_topRightProp[0] + center_bottomLeftProp[0] + center_bottomRightProp[0],
               center_topLeftProp[1] + center_topRightProp[1] + center_bottomLeftProp[1] + center_bottomRightProp[1],
               center_topLeftProp[2] + center_topRightProp[2] + center_bottomLeftProp[2] + center_bottomRightProp[2])

print("Center of Gravity: ", center_grav)
