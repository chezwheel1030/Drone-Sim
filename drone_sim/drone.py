from dataclasses import dataclass

@dataclass
class DroneProp:
    part: str
    weight: float # in kg
    #pos
    x: float
    y: float
    z: float
    
    thrust: float #ENwtons
    
@dataclass
class Drone:
    part: str
    weight: float # in kg
    #pos
    x: float
    y: float
    z: float
    

