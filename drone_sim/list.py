from drone import *

class PartList:
    topLeftProp = DroneProp("top leftpropeller", weight=0.5, x=-10.0, y=20.0, z=30.0, thrust=10.0)
    topRightProp = DroneProp("top right propeller", 0.5, 10.0, 20.0, 30.0, 10.0)
    bottomLeftProp = DroneProp("bottom left propeller", 0.5, -10.0, -20.0, 30.0, 10.0)
    bottomRightProp = DroneProp("bottom right propeller", 0.5, 10.0, -20.0, 30.0, 10.0)
    
    parts = [topLeftProp, topRightProp, bottomLeftProp, bottomRightProp]