# Program No: 03 Date: 24-04-2023
# Aim: write a python script to calculate the factorial of given number.
# Algorithm: 
# Step1. start 
# Step2. declare the value of num from the user 
# Step3. assaign a factorial variable is 1 
# Step4. .check a> I f num is less than zero 
# 1)if yes print factorial does not exist for -ve numbers. 
# b)elif num=0 
# 1)initialize i-1 
# 2) check if i yes, factorial-0 is 1 
# c)else <=n? 
# a) if yes, factorial-factorial*i 
# Step5. print the factorial 
# Step6. stop 
# Source Code:


num=int(input('Enter any number: ')) 
fact=1 
for i in range(1,num+1):
fact=fact*i
print('Factorial of',num,'=',fact

      
# Output:
# Enter any number: 5 
# Factorial of 5 = 120
# Result:
# successfully completed to display a factorial of given number
