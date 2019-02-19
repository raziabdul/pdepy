from enum import Enum
class Direction(Enum):
    POSITIVE = 1
    NEGATIVE = -1

class diff_operator(object):
    def __init__(self, stencil, coefficient = 1, is_time_dependent = False):
        # a list of tuple whose first element is relative position of node in the stencil, 
        # second element is the coefficient in the fdm equation
        self.stencil = stencil
        # the coefficient before this operator, e.g., 1/delta_x^2
        self.coefficient = coefficient
        self.is_time_dependent = is_time_dependent
    
    def getIrregularStencil(self, dx, tau, direction):
        raise NotImplementedError