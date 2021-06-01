import molecules
import numpy as np

coords = np.random.rand(2,11)

my_squiggle = molecules.dna(1, coords)

print("Molecule ID")
print(my_squiggle.id)

print("Co-ords")
print(my_squiggle.coordinates)

print("RoC - fake!")
print(my_squiggle.radius_of_curvature())