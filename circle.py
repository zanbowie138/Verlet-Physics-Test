import math
from shape import Shape
import utils

class Circle(Shape):
    def __init__(self, id, pos, size, color):
        Shape.__init__(self,id, pos,size, color)

    def applyConstraints(self):
        #Default constraints
        constraint_pos = [400,300]
        radius = 200
        
        #Vector between contstraint center and current position
        vector = utils.sub(self.pos_current, constraint_pos)

        #Distance between contstraint center and current position
        distance = utils.get_length(vector)

        #If circle is out of constraint
        if distance > (radius - self.size):
            #Direction of transformation
            unit_vec = utils.normalize(vector)

            #Distance of transformation
            distance_change = utils.mult_scalar(unit_vec, (radius-self.size))

            #Change current position by direction * distance
            self.pos_current = utils.add(constraint_pos,distance_change)
            