Aim: Write a Python program 
i.To create a set. 
ii.To remove item(s) from a set. iii. To remove an item from a set if it is present 
in the set. 
iv. To create a union and intersection of sets. v. To create set difference. 
Algorithm: 
i. To create a set: 
Step 1: Initialize an empty set. 
Step 2: Prompt the user to enter the number of elements they want to add. 
Step 3: Use a loop to iterate through the range of the number of elements. 
-Within the loop, prompt the user to enter each element. 
-Add each element to the set using the add() method. 
Step 4: The set is created successfully. 
ii. To remove item(s) from a set: 
Step 1: Prompt the user to enter the number of items they want to remove. 
Step 2: Use a loop to iterate through the range of the number of items. 
-Within the loop, prompt the user to enter each item. 
-Use the discard() method to remove each item from the set. 
Step 3: The items are removed successfully. 
iii.To remove an item from a set if it is present in the set: 
Step 1: Prompt the user to enter the item they want to remove. 
Step 2: Use the remove() method to remove the item from the set if it is present. 
Step 3: The item is removed successfully if it exists in the set. 
iv.To create a union and intersection of sets: 
Step 1: Create two sets, set1 and set2. 
Step 2: Use the union() method to create the union of set1 and set2. 
Step 3: Use the intersection() method to create the intersection of set1 and set2. 
Step 4: The union and intersection sets are created successfully. 
v.To create set difference: 
Step 1: Create two sets, set1 and set2. 
Step 2: Use the difference() method to create the set difference of set1 and set2. 
Step 3: The set difference is created successfully. 
Source code: 
i. To create a set 
set1={1,2,3,4} 
print(set1) 
Output: {1, 2, 3, 4} 
set2=set({1,2,3,4,1,2}) 
print(set2) 
Output: {1, 2, 3, 4} 
ii. To remove item(s) from a set. 
my_set={1,2,3,4} 
print(my_set) 
my_set.discard(4) 
print(my_set) 
Output: {1, 2, 3, 4} 
{1, 2, 3}
iii.To remove an item from a set if it is present in the set. 
my_set={1,2,3,4,5} 
print(my_set) 
my_set.remove(4) 
print(my_set) 
Output: 
{1, 2, 3, 4, 5} 
{1, 2, 3, 5} 
iv.To create a union and intersection of sets. 
# #Set union method 
# initialize A and B 
A= {1, 2, 3, 4, 5} 
B= {4, 5, 6, 7, 8} 
# use | operator 
print(A | B) 
Output: {1, 2, 3, 4, 5, 6, 7, 8} 
# Set Intersection 
A={1,2,3,4,5} 
B={3,5,6,7,8,9} 
# use & operator 
print(A&B) c
Output: {3, 5} 
v. To create set difference. 
# Set Difference 
# Difference of two sets 
# initialize A and B 
A= {1, 2, 3, 4, 5} 
B= {4, 5, 6, 7, 8} 
# use - operator 
print(A-B) 
Output: {1, 2, 3} 
Result: The programs of set operations are executed successfully
