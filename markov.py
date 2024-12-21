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
    transitionExp = np.matmul(transitionExp,transitionMatrix)

print("Matrix: \n", transitionExp, "\n")

nIterDist = np.matmul(startingDistribution, transitionExp)
print(nIterDist)


stableAfterMany = transitionMatrix
for i in range(10000):
    stableAfterMany = np.matmul(stableAfterMany, transitionMatrix)

print("Stable Matrix after 10000 Iterations: \n", stableAfterMany, "\n")


stableMatrix = startingDistribution
tresholdReached = False
iter = 0
while not tresholdReached:
    prevMatrix = stableMatrix
    iter = iter + 1
    stableMatrix = np.matmul(stableMatrix, transitionMatrix)
    diff = np.subtract(prevMatrix, stableMatrix)
    absDiff = np.array([abs(x) for x in diff]) 
    sumAbsDiff = np.sum(absDiff)
    if sumAbsDiff < 0.00000001:
        tresholdReached = True

print("Stable: \n",stableMatrix, "\n")
print("Iterations to Treshold Reached: ", iter)
