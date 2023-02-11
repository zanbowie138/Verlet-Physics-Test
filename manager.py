from circle import Circle
import utils

#Defines gravity
GRAVITY = [0.0,1000.0]

def applyGravity(circle):
    circle.accelerate(GRAVITY)

def update(sph_arr, dt):
    #Has substeps to increase accuracy
    substeps = 20
    sub_dt = dt / substeps

    for i in range(substeps):
        for circle in sph_arr:
            applyGravity(circle)
            circle.applyConstraints()
            resolve_collisions(sph_arr, circle)
            circle.updatePos(sub_dt)

def resolve_collisions(sph_arr, circle):
    #iterates through all circles in inputted array of Spheres
    for other in sph_arr:
        #Distance between this circle and circle in array
        distance = utils.get_distance(circle.pos_current, other.pos_current)

        #If distance between two circles is less than zero and it is not comparing to itself
        if distance < circle.size + other.size and not circle.equals(other):
            collision_axis = utils.get_unit_vec(circle.pos_current, other.pos_current)

            #How much the distance will change
            change_distance = (circle.size + other.size) - distance

            #Creates a vector along the collision axis, divided by two because 
            #both this circle and other circle will move in opposite directions 
            #in the same length
            change_vec = utils.mult_scalar(collision_axis, change_distance/2)

            #Moves circles away from each other
            circle.pos_current = utils.add(circle.pos_current, change_vec)
            other.pos_current = utils.sub(other.pos_current, change_vec)
