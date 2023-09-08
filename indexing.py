Aim: To write a python program array indexing such as slicing,integer array 
indexing and boolean array inedexing. 
Algorithm: 
Import the NumPy library: 
import numpy as np 
Create a NumPy array: 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
Array Slicing: 
# Syntax: arr[start:stop:step] 
# Get all elements from index 2 to the end 
sliced_arr = arr[2:] 
print(sliced_arr) 
# Output: [3, 4, 5, 6, 7, 8, 9, 10] 
# Get elements from index 1 to 5 with step 2 sliced_arr = arr[1:6:2] 
print(sliced_arr) 
# Output: [2, 4, 6] 
Boolean Array Indexing: 
# Create a boolean mask 
mask = np.array([True, False, True, False, False, True, False, True, False, True]) 
# Access elements where the mask is True boolean_indexed_arr = arr[mask]
print(boolean_indexed_arr) 
# Output: [1, 3, 6, 8, 10]
Source code: 
# Python program for basic slicing. 
import numpy as np 
# Arrange elements from 0 to 19 
a = np.arange(20) 
print("\n Array is:\n ",a) 
# a[start:stop:step] 
print("\n a[-8:17:1] = ",a[-8:17:1]) 
# The : operator means all elements till the end. 
print("\n a[10:] = ",a[10:]) 
Output: 
# Array is: 
# [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19] 
# a[-8:17:1] = [12 13 14 15 16] 
# a[10:] = [10 11 12 13 14 15 16 17 18 19] 
# Python program showing advanced indexing 
import numpy as np 
a = np.array([[1 ,2 ],[3 ,4 ],[5 ,6 ]]) 
print(a[[0 ,1 ,2 ],[0 ,0 ,1]]) 
# Output 
# [1 3 6] 
# Boolean Indexing import 
numpy as np 
a = np.array([10, 40, 80, 50, 100]) print(a[a>50]) 
Output: 
# [ 80 100] 
Result: write a python program array indexing such as slicing,integer array 
indexing and boolean array inedexing is executed successfully.
