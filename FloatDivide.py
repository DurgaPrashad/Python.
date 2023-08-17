# Write a Python program that prompts the user for two floating-point 
# values and displays the result of the first number divided by the second with 
# exactly six decimal places displayed.
# Algorithm:
# Step1. Start the program. 
# Step2. Prompt the user to enter a floating point number and store it in the 
# variable n1. 
# Step3. Prompt the user to enter another floating point number and store it in the 
# variable n2. 
# Step4. Calculate the division of n1 by n2 and store the result in a temporary 
# variable temp. 
# Step5. Print the result using string formatting with 6 decimal places: "n1/n2 = 
# %.6f" % temp. 
# Step6. End the program.
# Source Code:

n1=float(input('Enter a floating point number: ')) 
n2=float(input('Enter a floating point number: ')) 
print('n1/n2=%.6f'%(n1/n2)) 

# Output:
# Enter a floating point number: 12.5 
# Enter a floating point number: 3.5 
# n1/n2=3.571429 
# Result:
# Successfully completed to display floating values numbers.
