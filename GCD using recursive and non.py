# AIM: Write a python script to find GCD of two numbers using recursive and 
# non-recursive functions. 
# Algorithm: 
# Recursive function: 
# Step 1: Define a function gcd_recursive(a, b) that takes two numbers as input. 
# Step 2: Check if a is equal to 0. 
# -If yes, return the value of b. 
# Step 3: Otherwise, recursively call the gcd_recursive function with arguments b 
# and the remainder of b divided by a. 
# Step 4: Return the result of the recursive call. 
# Non- recursive function: 
# Step 1: Define a function gcd_non_recursive(a, b) that takes two numbers as 
# input. 
# Step 2: Use a loop to continue until a is equal to 0. 
# -Calculate the remainder of b divided by a and store it in a temporary variable. 
# -Assign the value of a to b and the value of the remainder to a. 
# Step 3: Return the value of b, which will be the GCD of the two numbers. 
# Source code: 
# Recursive Function(Euclid's Algorithm) 

def gcd(a,b): 
if a==0: 
return b 
else: 
return gcd(b%a,a)
a=int(input('Enter the First Number: ')) 
b=int(input('Enter the Second Number: ')) 
print('The gcd of',a,'and',b,'is',gcd(a,b)) 

# Output: 
# # Enter the First Number: 15 
# # Enter the Second Number: 20 
# # The gcd of 15 and 20 is 5 
def gcd(a, b): 
if a > b: small = b 
else: 
small = a 
for i in range(1, small+1): 
if((a % i == 0) and (b % i == 0)): 
gcd = i 
return gcd 
a = int(input('Enter the first number: ')) 
b= int(input('Enter the second number: ')) 
print ("The gcd of {} and {} is {} ".format(a,b,gcd(a,b))) 
Output: 
# Enter the first number: 20 
# Enter the second number: 15 
# The gcd of 20 and 15 is 5 
# RESULT: python script to find GCD of two numbers using recursive and nonrecursive functions executed successfully.
