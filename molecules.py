import numpy as np

class molecule():
    def __init__(self, id):
        self.id = id

class dna(molecule):
    def __init__(self, id, coordinates):
        super().__init__(id)
        self.coordinates = coordinates

    def radius_of_curvature(self):
        return (np.sum(self.coordinates))

class protein(molecule):
    def __init__(self, id):
        super().__init__(id)