#extract all odd numbers from array

import numpy as np

#assign an array
arr = np.array([1,2,3,4,5,6,7,8,9,10])

#extract odd numbers from array
odd_num = np.extract(arr%2 !=0, arr)
print("The odd elements in the array are: ", odd_num)
