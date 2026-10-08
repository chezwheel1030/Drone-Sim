from drone import *

class partList:
    topLeftProp = drone("top leftpropeller", 0.5, -10.0, 20.0, 30.0)
    topRightProp = drone("top right propeller", 0.5, 10.0, 20.0, 30.0)
    bottomLeftProp = drone("bottom left propeller", 0.5, -10.0, -20.0, 30.0)
    bottomRightProp = drone("bottom right propeller", 0.5, 10.0, -20.0, 30.0)
    
    list = [topLeftProp, topRightProp, bottomLeftProp, bottomRightProp]