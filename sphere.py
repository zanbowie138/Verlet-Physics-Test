import math
from shape import Shape
import utils

class Sphere(Shape):
    def __init__(self, id, pos, size, color):
        Shape.__init__(self,id, pos,size, color)

    def applyConstraints(self):
        constraint_pos = [400,300]
        radius = 200
        
        vector = utils.sub(self.pos_current, constraint_pos)
        distance = utils.get_length(vector)
        if distance > (radius - self.size):
            unit_vec = utils.normalize(vector)
            distance_change = utils.mult_scalar(unit_vec, (radius-self.size))
            self.pos_current = utils.add(constraint_pos,distance_change)
            