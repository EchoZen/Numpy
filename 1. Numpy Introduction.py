import numpy as np
height= [1.73, 1.68, 1.71,1.89,1.79]
weight= [65.4,59.2,63.6,88.4,68.7]
np_height= np.array(height)
np_weight= np.array(weight)
print(np_height)
print(np_weight)

bmi= np_weight/np_height**2
print(bmi)

# numpy can only contain 1 type of data (it will auto convert to one type)
# numpy will add elements according to the index, while lists added together will extend the list (appending)
# numpy works like a list, you can call on the index to get the element

print(bmi>23) # Returns booleans of elements >23
print(bmi[bmi>23]) # Returns array of elements >23



