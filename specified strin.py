# Aim: Write a Python script to get a string made of 4 copies of the last two 
# characters of a specified string (length must be at least 2). 
# Sample Input /Output 
# Input: Python –Output:onononon 
# Input: Exercises Output: eseseses 
# Algorithm: 
# Step 1: Prompt the user to enter a string. 
# Step 2: Read the input from the user and store it in a variable. 
# Step 3: Check if the length of the input string is at least 2. 
# - If the length is less than 2, display an error message and end the algorithm. 
# Step 4: Get the last two characters of the input string using slicing. 
# Step 5: Create a new string by concatenating the last two characters four times. 
# Step 6: Display the resulting string to the user. 
# Source code: 

str=input('Enter any word: ') 
print(str[-2:]*4) 

# Output: 
# Enter any word: Python onononon 
# Result: Python script to get a string made of 4 copies of the last two characters 
# of a specified string (length must be at least 2). Executed
