# Aim: Write a program to demonstrate working with dictionaries in Python 
# Algorithm: 
# 1.Create an empty dictionary `my_dict`. 
# 2.Add key-value pairs to the dictionary using the assignment operator `=`. For 
# example, `my_dict[key] = value`. 
# 3.Access the value of a specific key by using the key inside square brackets. For 
# example, `my_dict[key]`. 
# 4.Update the value of an existing key by assigning a new value to it. For 
# example, `my_dict[key] = new_value`. 
# 5.Check if a key exists in the dictionary using the `in` operator. For example, 
# `key in my_dict`. 6. Remove a key-value pair from the dictionary using the `del` 
# statement. For example, `del my_dict[key]`. 
# 7. Iterate over the keys, values, or key-value pairs in the dictionary using a `for` 
# loop and the appropriate dictionary method. For example, `for key in 
# my_dict.keys():` or `for value in my_dict.values():` or `for key, value in 
# my_dict.items():`. 
# Source code: 

# Creating a Python Dictionary 
# Empty Dictionary 
my_dict={} 
print(my_dict) 
Output: {} 


# dictionary with items 
dict1={1:'apple',2:'banana',3:'pears',4:'guava'} 
print(dict1) 
Output: {1: 'apple', 2: 'banana', 3: 'pears', 4: 'guava'} 

# dictionary with mixed keys 
my_dict = {'name': 'John', 1: [2, 4, 3]} print(my_dict) 
Output: {'name': 'John', 1: [2, 4, 3]} 


# using dict() to create dictionary 
dict1=dict({'name':'Jack','age':24,'dept':'CSM'}) 
print(dict1) print(type(dict1)) 
Output: 
{'name': 'Jack', 'age': 24, 'dept': 'CSM'} 
<class 'dict'> 


# Accessing Elements from Dictionary 
# While indexing is used with other data types to access values, # a dictionary 
# uses keys. Keys can be used either inside square brackets [] # or with the get() 
# method. 
day={'sun':'Sunday','mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Th 
ursday', 
'fri':'Friday','sat':'Saturday'} 
print(day['sun']) 
print(day['mon']) print(day['sat']) 
Output: 
Sunday 
Monday 
Saturday 

# using get() 
print(day.get('sun')) print(day.get('fri')) 
print(day.get('st')) 
Output: 
Sunday 
Friday 
None 


# Changing and Adding values 
my_dict = {'name': 'Jack', 'age': 26} print(my_dict) # update value 
my_dict['age']=27 print(my_dict) 
Output: 
{'name': 'Jack', 'age': 26} 
{'name': 'Jack', 'age': 27} 


# adding items in my_dict 
my_dict['gender']='Male' 
print(my_dict) 
Output: {'name': 'Jack', 'age': 27, 'gender': 'Male'} 

# Removing elements from Dictionary 
# We can remove a particular item in a dictionary # by using the pop() method. 
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} print(squares) print(squares.pop(5)) 
Output: 
Before pop(): {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
 

popped value: 1 
# by using popitem() 
print(squares.popitem()) 
print(squares) 
Output: 
Before popitem(): {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
popitem(): (5, 25) 
After popitem(): {1: 1, 2: 4, 3: 9, 4: 16} 

# using clear() 
squares.clear() 
print(squares) 
Output: 
Before clear(): {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

# After clear(): {} 
# using del keyword -delete the dictionary itself del squares print(squares) 
Output: 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
Traceback (most recent call last): 
File "c:/Users/Dell/hello/Week 6.py", line 94, in <module> 
print(squares) 
NameError: name 'squares' is not defined 
 

# Dictionary Method- items(),keys(),values() 
dict={'name':'John','age':28,'adrress':'church street','city':'Chittoor','stat e':'AP'} 
print(dict.keys()) #To get the keys in dictionary 
Output: 
dict_keys(['name', 'age', 'adrress', 'city', 'state']) 
#To get the values in the dictionary 
print(dict.values) 
Output: 
dict_values(['John', 28, 'church street', 'Chittoor', 'AP']) 
print(dict.items()) 
Output: 
dict_items([('name', 'John'), ('age', 28), ('adrress', 'church street'), ('c ity', 
'Chittoor'), ('state', 'AP')]) 
# Dictionary Comprehension 
# creating dict whose value is square of its key squares={i:i*i for i in 
range(1,11)} print(squares) 
# Output 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100} 
# creating dict whose value is cube of its key cube={x:x**3 for x in range(6)} 
print(cube) 
Output: 
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125} 

# creating a new dictionary from the old dictionary using comprehension 

player={'john':45,'luka':38,'rocky':58,'jill':28,'sohan':18,'christiano':33,'messi':34} 
old_player={k:v for k,v in player.items() if v>40 } print(old_player) 
Output: 
{'john': 45, 'rocky': 58} 


# Iterating through Dictionary 
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81} 
for i in squares: 
print(squares[i]) 
Output: 
1 
9 
25 
49 
81 
RESULT: programs to demonstrate working with dictionaries in Python is 
successfully executed
