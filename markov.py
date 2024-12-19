import numpy as np
 
states = ["A", "B", "C"]
 
transitionMatrix = np.array([[0.3, 0.6, 0.1], [0.2, 0.6, 0.2], [0.2,0.3,0.5]])
startingDistribution = np.array([0.4, 0.5, 0.1]) 
state = np.random.choice([0,1,2], p=startingDistribution)
 
print(states[state], "->", end=" ")
 
for i in range(20):
    state = np.random.choice([0, 1, 2], p=transitionMatrix[state])
    print(states[state], "->", end=" ")
print("end")
