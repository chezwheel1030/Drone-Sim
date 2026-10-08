from list import *

total_x = 0
total_y = 0
total_z = 0
total_weight = 0

class Center:
    for part in PartList.parts:
        total_x += part.x * part.weight 
        total_y += part.y * part.weight
        total_z += part.z * part.weight
        total_weight += part.weight
        
    center_x = total_x / total_weight
    center_y = total_y / total_weight
    center_z = total_z / total_weight
    centerGrav = [center_x, center_y, center_z]
    print(centerGrav) 
        
