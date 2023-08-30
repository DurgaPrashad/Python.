# Aim: Write a Python program to replace last value of tuples in a list. 
# Algorithm: 
# 1.Create an empty list `modified_list` to store the modified tuples. 
# 2.Iterate over each tuple `tuple_item` in the input list `tuples_list`. 
# 3.Get all the elements of the tuple except the last one using the slicing notation 
# `tuple_item[:1]`. 
# 4.Create a new tuple by concatenating the sliced tuple with the new value using 
# the tuple concatenation operator `+` and the tuple constructor `()`. 
# 5.Append the modified tuple to the `modified_list`. 
# 6.Return the `modified_list` as the result. 
# Source code: 

list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
print([x[:-1] + (100,) for x in list1]) 

# Output: 
# [(10, 20, 100), (40, 50, 100), (70, 80, 100)] 
# RESULT: Python program to replace last value of tuples in a list is successfully 
# executed
