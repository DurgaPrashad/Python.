# Aim: Write a python script to display the prime number series up to the given N 
# Value.
# Algorithm: 
# 1.Start the program. 
# 2.Prompt the user to enter the value of N and store it in the variable N. 
# 3.Print the message "Prime number series up to N:". 
# 4.Initialize an empty list named "primes" to store the prime numbers. 
# 5.Iterate through the numbers from 2 to N (inclusive) using a for loop: 
# - Inside the loop, perform the following steps: 
# -Initialize a boolean variable named "is_prime" and set it to True. 
# -Iterate through the numbers from 2 to the square root of the current number 
# (using the math library or another approach) using a nested for loop: 
# -Inside the nested loop, check if the current number is divisible by any number 
# from 2 to the square root of the current number. If true, set "is_prime" to False 
# and break out of the loop. 
# -After the nested loop, check if "is_prime" is still True: 
# -If true, the current number is prime. Append it to the "primes" list. 
# 6.Print the prime numbers in the "primes" list using the join() function to 
# concatenate the numbers into a single string, separated by commas. 
# 7.End the program.
# Source code: 

def isPrime(n):
if n<=1:
return False
for i in range(2,n):
if n%i==0:
return False
return True
n=int(input('Enter the number: '))
for x in range(2,n+1):
if isPrime(x):
print(x,end=' ')

# Output:
# Enter the number: 10
# 2 3 5 7
# Result:
# Python script to display the prime number series executed successfully.
