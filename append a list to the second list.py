# Aim: To append a list to the second list. 
# v. To append a list to the second list. 
# Algorithm: 
# 1.Initialize `list1` with the given elements: `['apple', 'banana', 'mango', 'pears', 
# 'cherry', 'guava']`. 
# 2.Initialize `list2` with the given elements: `['rose', 'china rose', 'sunflower']`. 
# 3.Iterate over each element `i` in `list1`: 
# - Append `i` to `list2` using the `append()` method. 
# 4.Print `list1`. 5. Print `list2`. 
# Source code: 

list1=['apple','banana','mango','pears','cherry','guava'] 
list2=['rose','china rose','sunflower'] 
for i in list1: 
list2.append(i) 
print(list1) 
print(list2) 

# Output: 
# ['apple', 'banana', 'mango', 'pears', 'cherry', 'guava'] 
# ['rose', 'china rose', 'sunflower', 'apple', 'banana', 'mango', 'pears', 'cher ry', 
# 'guava'] 
# RESULT: The program to append list is successfully executed
