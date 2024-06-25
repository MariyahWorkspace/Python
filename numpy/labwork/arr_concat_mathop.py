import numpy as np

#1. Concatenate two arrays------------------------------------->

print("------------CONCATENATION OF ARRAYS---------------------")

#create/assign arrays
ar1 = np.array([1, 2, 3, 4, 5])
ar2 = np.array([6, 7, 8, 9, 10])
#print arrays
print("The two arrays are:")
print("Array 1: ", ar1)
print("Array 2: ", ar2)

#concatenate using 'concatenate' module
concat_arr = np.concatenate([ar1, ar2])
print("Concatenated array is: ", concat_arr,
        "\n(using concatenate module)\n")

#concatenate using '+' operator
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]
concat_array = array1 + array2
print("Concatenated array is: ", concat_array,
        "\n(using '+' operator)\n")

#2. Mathematical operations on array------------------------------>

print("------------MATHEMATICAL OPERATIONS ON ARRAYS---------------------")

#create/assign two arrays
arr1 = np.array([11, 4, 34, 28])
arr2 = np.array([5, 2, 17, 14])
print('The two arrays under operation are:')
print("Array 1: ", arr1)
print("Array 2: ", arr2)
print("\n")

#using mathematical operation '+'
res_arr1 = arr1 + arr2
print("The result of '+' operator on arrays:\n",
        res_arr1,"\n")
        
#using mathematical operation '-'
res_arr2 = arr1 - arr2
print("The result of '-' operator on arrays:\n",
        res_arr2,"\n")
        
#using mathematical operation '*'
res_arr3 = arr1 * arr2
print("The result of '*' operator on arrays:\n",
        res_arr3,"\n")

#using mathematical operation '/'
res_arr4 = arr1 / arr2
print("The result of '/' operator on arrays:\n",
        res_arr4,"\n")        
        
#using mathematical operation '%'
res_arr5 = arr1 % arr2
print("The result of '%' operator on arrays:\n",
        res_arr5,"\n")
        
#using mathematical operation '**'
res_arr6 = arr1 ** 2
print("The result of '**' (exponent) operator on arrays:\n",
        res_arr6,"\n")


