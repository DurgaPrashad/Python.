# AIM: Write a python script to demonstrate the Exception Handling
# Algorithm: 
# Step 1: Prompt the user to enter a number. 
# Step 2: Read the input from the user and store it in a variable. 
# Step 3: Wrap the code that may potentially raise an exception inside a try block. 
# Step 4: In the try block, attempt to perform the desired operation. 
# -If an exception occurs, the program will jump to the except block. 
# -Handle the exception by providing appropriate error messages or performing 
# necessary actions. 
# Step 5: If no exception occurs, the code after the try-except block will be 
# executed. 
# Step 6: Optionally, include a finally block to execute code that must always run, 
# regardless of whether an exception occurred or not. 
# Step 7: End the program. 
# Source code:
try: 
print(x) 
except: 
print('An exception occurs') 
finally: 
print('I am in finally block') 
Output: 
# An exception occurs 
# I am in finally block 
try: 
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: ')) 
print(a/b) 
except Exception as e: 
print('Number should not be divided by zero') 
print('Exception Class:',e) 
Output: 
# Enter the first number: 10 
# Enter the second number: 0 
# Number should not be divided by zero 
# Exception Class: division by zero 
# Multiple exception 
try: 
x=10 
print(y) 
except NameError: 
print('Variable x is not defined') 
except: 
print('Something is Wrong') 
else: 
print('All is well') 
# Output: 
# # Variable x is not defined 
# RESULT: Python script to demonstrate the Exception Handling Executed 
# successfully.
