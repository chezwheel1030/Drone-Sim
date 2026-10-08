from drone import *

class PartList:
    topLeftProp = Drone("top leftpropeller", weight=0.5, x=-10.0, y=20.0, z=30.0, thrust=10.0)
    topRightProp = Drone("top right propeller", 0.5, 10.0, 20.0, 30.0, 10.0)
    bottomLeftProp = Drone("bottom left propeller", 0.5, -10.0, -20.0, 30.0, 10.0)
    bottomRightProp = Drone("bottom right propeller", 0.5, 10.0, -20.0, 30.0, 10.0)
    
    parts = [topLeftProp, topRightProp, bottomLeftProp, bottomRightProp]