# Aim: Program to perform Basic Arithmetic on Two numbers from math import 
# log10.
# Algorithm: 
# Step1. start 
# Step2. print ***Arithmatic operations*** 
# Step3. n1=(int)input from user,enter the value n: 
# Step4. n2=(int)input from user,entyer the value of n2 
# Step5. sum=n1+n2; diff=n1-n2; mul=n1*n2; div=n1/n2; power=n1**n2; 
# floordiv=n1//n2; mod=n1%n2 
# Step6. print sum, diff, product, div, exponents, floor_division, modules 
# Step7. Stop
# Source Code:
n1=int(input('Enter the First Number: ')) 
n2=int(input('Enter the Second Number:’)) 
sum=n1+n2 
diff=n1-n2 
mult=n1*n2 
div=n1/n2 
expon=n1**n2 
print('Sum of ',n1,'and',n2,'is: ',sum) 
print('Difference of ',n1,'and',n2,'is:',diff) 
print('Multiplication of ',n1,'and',n2,'is:',mult) 
print('Division of ',n1,'by',n2,'is:',format(div,'.2f')) 
print( n1,'raised to ',n2,'is: ',expon) 
print('log10 of ',n1,'is %.2f'%log10(n1))
..............................................................................
# Output:
# Enter the First Number: 10 
# Enter the Second Number: 5 
# Sum of 10 and 5 is: 15 
# Difference of 10 and 5 is: 5 
# Multiplication of 10 and 5 is: 50 
# Division of 10 by 5 is: 2.00 
# 10 raised to 5 is: 100000 
# log10 of 10 is 1.00
# Result:
# successfully completed python program on basic arithmetic operations
