# Aim: Write a python script to arrange the given list of elements in ascending or 
# descending order. 
# Algorithm: 
# 1.Initialize the list with the given elements. 
# 2.Prompt the user to choose the sorting order (ascending or descending). 
# 3.If the user chooses ascending order: 
# - Use the `sort()` method to sort the list in ascending order. 
# 4. If the user chooses descending order: 
# - Use the `sort()` method with the `reverse=True` argument to sort the list in 
# descending order. 
# 5. Print the sorted list. 
# Source code: 

list1=[45,12,6,78,91,87] 
print('Original List',list1) 
list1.sort() 
print('List of elements in ascending order',list1) 
list1.reverse() 
print('List of elements in descending order',list1) 

# Output: 
# Original List [45, 12, 6, 78, 91, 87] 
# List of elements in ascending order [6, 12, 45, 78, 87, 91] 
# List of elements in descending order [91, 87, 78, 45, 12, 6] 
# Result: The list of elements in ascending or descending order is executed 
# successfully
