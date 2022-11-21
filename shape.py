import utils

class Shape():
    def __init__(self, id, pos, size, color):
        self.id = id
        self.color = color
        self.pos_current = pos
        self.size = size
        self.pos_old = pos
        self.acceleration = [0.0,0.0]


    def updatePos(self, dt):
        #Get velocity
        velocity = utils.sub(self.pos_current,self.pos_old)

        #Save current position
        self.pos_old = self.pos_current

        #Perform Verlet Integration
        self.pos_current = utils.add(self.pos_current,velocity,utils.mult_scalar(self.acceleration, dt * dt))

        #Reset acceleration
        self.acceleration = [0.0,0.0]
    
    def applyConstraints(self):
        pass
    
    def accelerate(self, acc):
        #Adds acceleration
        self.acceleration = utils.add(self.acceleration,acc)

    def getPositionX(self):
        return int(self.pos_current[0])

    def getPositionY(self):
        return int(self.pos_current[1])

    def equals(self, other):
        #Compares this shape's id to other shape's id
        if (self.id == other.id):
            return True
        else:
            return False