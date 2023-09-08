AIM: Write a program to demonstrate a) arrays b) array indexing such as 
slicing, integer array indexing and Boolean array indexing along with their basic 
operations in NumPy. 
Algorithm: 
1)Import numpy library: 
import numpy as np 
2)create numpy array: 
arr = np.array([1, 2, 3, 4, 5]) 
3)create numpy arary: 
arr = np.array([1, 2, 3, 4, 5]) 
4)boolian array indexing: 
mask = np.array([True, False, True, False, True]) 
print(arr[mask]) 
5)Array Slicing: 
# Syntax: arr[start:stop:step] 
# Get all elements from index 2 to the end 
sliced_arr = arr[2:] 
print(sliced_arr) 
# Output: [3, 4, 5, 6, 7, 8, 9, 10] 
# Get elements from index 1 to 5 with step 2 sliced_arr = arr[1:6:2] 
print(sliced_arr) 
# Output: [2, 4, 6] 
6)Boolean Array Indexing: 
# Create a boolean mask 
mask = np.array([True, False, True, False, False, True, False, True, False, True]) 
# Access elements where the mask is True boolean_indexed_arr = arr[mask] 
print(boolean_indexed_arr) 
# Output: [1, 3, 6, 8, 10]
Source code:
a)arrays 
import numpy as np 
a= np.array([1,2,3,4]) 
print(a) 
# Output 
# [1 2 3 4] 
import numpy as np 
b=np.array([(1,2,3),(4,5,6)]) 
print(b) 
Output: 
# [[1 2 3] 
# [4 5 6]] 
RESULT: program to demonstrate a) arrays b) array indexing such as slicing, 
integer array indexing and Boolean array indexing along with their basic 
operations in NumPy as executed successfully
