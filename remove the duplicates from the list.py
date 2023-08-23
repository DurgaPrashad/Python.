# Aim: To remove the duplicates from the list Program. 
# ii . To remove duplicates from a list. 
# Algorithm: 
# 1.Start the program. 
# 2.Create a list with duplicate elements and store it in a variable named 
# "original_list". 
# 3.Create an empty list named "unique_list" to store the unique elements. 
# 4.Iterate through each element in the "original_list" using a for loop: 
# -Inside the loop, check if the current element is already in the "unique_list": 
# -If it is not in the "unique_list", append the element to the "unique_list". 
# 5.After the loop, the "unique_list" will contain only the unique elements from 
# the "original_list". 
# 6.Print the "unique_list" to display the list without duplicates. 
# 7.End the program. 
# Source code: 

dup_list=[1,2,3,4,1,1,2,3,4,5,5,6,7,8,9] 
new_list=[] 
for i in dup_list: 
if i not in new_list: 
new_list.append(i) 
print('New List: ',new_list) 

# Output: 
# New List: [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# RESULT: To remove the duplicates from the list executed successfully
