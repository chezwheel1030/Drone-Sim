class airRes: 
    p = 0 # Air density  (kg/m^3)
    v = 0 # Object speed reltive to air (m/s)
    cd = 0 # Drag Coeffcient
    a = 0 # Refrence Area
    
    dragforce = .5 * p * (v^2) * cd * a