import numpy as np
import scipy.linalg
from numpy.linalg import matrix_power
states = ["A", "B", "C"]
 
transitionMatrix = np.array([[0.3, 0.6, 0.1], [0.2, 0.6, 0.2], [0.2,0.3,0.5]])
startingDistribution = np.array([0.4, 0.5, 0.1]) 
state = np.random.choice([0,1,2], p=startingDistribution)
 
print(states[state], "->", end=" ")
 
for i in range(100):
    state = np.random.choice([0, 1, 2], p=transitionMatrix[state])
    print(states[state], "->", end=" ")
print("end")

transitionExp = transitionMatrix
for i in range(4):
    print(i)
    transitionExp = np.matmul(transitionExp,transitionMatrix)

print("Matrix: \n", transitionExp, "\n")

nIterDist = np.matmul(startingDistribution, transitionExp)
print(nIterDist)
stable = np.matmul(startingDistribution, transitionExp)
print("Stable: ", stable)
randomStart = np.array([0.1, 0.9, 0.0]) 
stable2 = np.matmul(randomStart, transitionExp)
print("Stable: ", stable2)

stableMatrix = startingDistribution
for i in range(90):
    stableMatrix = np.matmul(stableMatrix, transitionMatrix)

print(stableMatrix)