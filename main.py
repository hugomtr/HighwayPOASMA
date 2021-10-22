import matplotlib.pyplot as plt
import numpy as np
import copy


def carte_implementation():
    nsroad1 = np.array([5,11,18,28,37,43,49,59,76,89,95])
    nsroad2 = nsroad1+1
    ewroad1 = np.array([7,13,22,45,67,78,90])
    ewroad2 = ewroad1+1
    mat = np.zeros((100,100))

    for c in nsroad1:
        mat[:,c] += 1
    for l in ewroad1:
        mat[l,:] += 1

    for c in nsroad2:
        mat[:,c] += 3
    for l in ewroad2:
        mat[l,:] += 3
        
    return city

matsens1 = carte_implementation()
feu = copy.deepcopy(matsens1)
"""
See the matrix

plt.imshow(city)
plt.show()
"""

