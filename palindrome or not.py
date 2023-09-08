# AIM: Write a Python function that checks whether a passed string is 
# palindrome or not. 
# Algorithm: 
# Step 1: Prompt the user to enter a string. 
# Step 2: Read the input from the user and store it in a variable. 
# Step 3: Initialize two pointers, one pointing to the start of the string and the 
# other pointing to the end of the string. 
# Step 4: Use a loop to compare the characters at the two pointers. 
# -If the characters are not equal, display that the string is not a palindrome and 
# end the algorithm. 
# -Move the start pointer one step forward and the end pointer one step backward. 
# -Repeat the comparison until the pointers meet or cross each other. 
# Step 5: If the loop completes without breaking, display that the string is a 
# palindrome. 
# Source code: 

def palin(str): 
if str==str[::-1]: 
print(str,'is a Plaindrome') 
else: 
print(str,'is not a Palindrome') 
str1=input('Enter any string: ') 
palin(str1) 

# Output: 
# Enter any string: MadaM 
# MadaM is a Plaindrome 
# RESULT: Python function that checks whether a passed string is palindrome or 
# Executed successfully
