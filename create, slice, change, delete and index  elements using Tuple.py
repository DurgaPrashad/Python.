# Aim: To write a python program to create, slice, change, delete and index 
# elements using Tuple. 
# Algorithm: 
# 1.Create an empty tuple using the `tuple()` constructor. 
# 2.Print the type of `tup1` using the `type()` function. 
# 3.Index the elements of the tuple: 
# -Print the first element of `tup1` using index `0`. 
# -Print the last element of `tup1` using index `-1`. 
# 4.Define a new tuple `tup2` with the given elements. 
# 5.Perform slicing on `tup2`: 
# -Print elements from the 2nd to the 4th index using slicing `[1:4]`. 
# -Print elements from the beginning to the 2nd index using slicing `[:2]`. 
# -Print all elements of `tup2` using slicing `[:]`. 
# 6.Attempt to change an element of `tup2` by assigning a new value to the 0th 
# index: 
# - Note that this operation will raise a `TypeError` because tuples are immutable. 
# 7.Attempt to delete an element from `tup2` by using the `del` statement: 
# - Note that this operation will raise a `TypeError` because tuples do not support 
# item deletion. 
# Source code: 

# create a tuple 
tup1=tuple() 
print(type(tup1)) 
# Output: 
# #<class 'tuple'> 
# # index elements 


tup1=('P','y','t','h','o','n') 
print(tup1[0]) 
print(tup1[-1]) 
# Output: 
# #P 
# #n 


# Slicing 
tup2=('P','r','o','g','r','a','m','m','e','r') 
# Element 2nd to 4th 
print(tup2[1:4]) 
#Output: ('r','o','g') 

# elements beginning to 2nd 
print(tup2[:2]) 
Output: ('P', 'r') 
# elements beginning to end 
print(tup2[:]) 
Output: ('P','r','o','g','r','a','m','m','e','r') 


# Changing the element 
tup2=('P','r','o','g','r','a','m','m','e','r') 
tup2[0]='L' 
print(tup2) 
Output:
#Traceback (most recent call last): 
#File "c:/Users/Dell/hello/Week 5.py", line 35, in <module> 
Program No: 12 Date: 08-05-2023
Tup2[0]=`L`
TypeError: `tuple` object does not support item assignment


# Deleting the Element 
tup2=('P','r','o','g','r','a','m','m','e','r') 
del tup2[0] 
print(tup2) 
Output: 
Traceback (most recent call last): 
File "c:/Users/Dell/hello/Week 5.py", line 47, in <module> 
del tup2[0] 
TypeError: 'tuple' object doesn't support item deletion 
Result: To write a python program to create, slice, change, delete and index 
elements using Tuple is successfully executed
