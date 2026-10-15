from airRes import *
from drone import *
from list import *
from PartFunction import *

print("List: ")
for part in PartList.parts:
    print(f"{part.part}, ", end="")
print("")
print("")

print(f"Center of Gravity: {CenterGrav.centerGrav}")
print("")

print("Air Resistance")
print(f"Air Density: {AirRes.p} kg/m^3")
print(f"Speed: {AirRes.v} m/s")
print(f"Drag Coeffcient: {AirRes.cd}")
print(f"Refrence Area: {AirRes.a}")
print(f"Drag Force: {AirRes.dragForce}")
print("")

print(f"Torque: {Torque.torque_total}")