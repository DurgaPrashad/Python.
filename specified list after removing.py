# Aim: Write a Python program to print a specified list after removing the 0th, 4th 
# and 5th elements. 
# Algorithm: 
# 1.Initialize the specified list with the given elements. 
# 2.Use the `del` statement to remove the 5th element. 3. Use the `del` statement 
# to remove the 4th element. 
# 4.Use the `del` statement to remove the 0th element. 
# 5.Print the modified specified list. 
# Source code: 


Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
Expected Output : ['Green', 'White', 'Black'] 
colors=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
new_colors=[] 
for i,x in enumerate(colors): 
if i not in (0,4,5): 
new_colors.append(x) 
print(new_colors) 

# Output: 
# ['Green', 'White', 'Black'] 
# Result: Python program to print a specified list after removing the 0th, 4th and 
# 5th elements is successfully executed.
