from PartFunction import *
from list import *

class AirRes: 
    p = 0 # Air density  (kg/m^3)
    v = 0 # Object speed reltive to air (m/s)
    cd = 0 # Drag Coeffcient
    a = 0 # Refrence Area
    
    dragForce = .5 * p * v**2 * cd * a

class Torque:
    torque_x = 0
    torque_y = 0
    torque_z = 0

    for prop, offset in zip(PartList.propParts, OffSet.offsets):
        offset_x, offset_y, offset_z = offset

        torque_x += offset_y * prop.thrust
        torque_y -= offset_x * prop.thrust

    torque_total = [torque_x, torque_y, torque_z]
    #print(torque_total)