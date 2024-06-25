#create array elements between 25 to 45(20 elements)

import numpy as np

arr = np.arange(25,45)
print("The array of 20 elements is: \n", arr)
print("The size of array is", arr.size, "elements.\n")

#arranging them in equal sizes
#we will divide the array in 4 sub-arrays of equal size (5 element each)
sub_arr = arr.reshape(4,5)
print("The equal sized arrays are:\n", sub_arr)
