import numpy as np
np_2d= np.array([[1.73, 1.68, 1.71,1.89,1.79], [65.4,59.2,63.6,88.4,68.7]])
print(np_2d.shape)
print(np_2d)

# Subsetting to obtain the elements
# 1st way
print(np_2d[0][1])
# 2nd way
print(np_2d[0,1]) # row, column

# To get numbers from 1st and 2nd column, 1st and 2nd row
print(np_2d[:,1:3]) # 3rd is not included

# Get average
print(np.mean(np_2d[:,0])) # Lets you slice out which part you want for the mean

print(np.corrcoef(np_2d[:,0],np_2d[:,1]))
print(np.std(np_2d[:,0], np_2d[:,1])

# Simulation
height= np.round(np.random.normal(1.75,0.2,5000),2) # Distribution mean, std deviation, no. of samples
weight= np.round(np.random.normal(60.32,15,5000),2)
np_city= np.column_stack((height, weight))
