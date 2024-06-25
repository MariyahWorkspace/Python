#find array elements greater than 10

import numpy as np

#assign array using np
arr = np.array([2, 5, 11, 25, 67, 4, 44, 8])

#extract elements greater than 10
print("The given array: ", arr)
req_arr = np.extract(arr > 10, arr)
print("Elements greater than 10 are: ", req_arr,"\n\n")

#replace items that satisfy a condition without affecting the original array

#create/assign an array
print("Replacing elements of original array")
print("Original array: ", arr)

#replace all elements that satisfy a condition
#suppose our condition is replacing elements that are greater than 20
arr[arr > 20] = 0
print("Replaced array: ", arr,
      "\n(with all elements greater than 20 replaced with 0)")

