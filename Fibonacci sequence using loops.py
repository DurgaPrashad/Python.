# Aim: Write a python script to display Fibonacci sequence of numbers using 
# while loop, for loop and dowhile loop constructs.
# #Fibonacci series using while loop
# Algorithm:
# Step1. Start the program. 
# Step2. Prompt the user to enter the number of terms they want in the Fibonacci 
# sequence and store it in the variable nterms. 
# Step3. Initialize the variables n1 and n2 to 0 and 1, respectively, which 
# represent the first two terms of the Fibonacci sequence. 
# Step4. Print the message "Fibonacci sequence:". 
# Step5. Initialize a counter variable count to 0. 
# Step6. Enter a while loop with the condition count < nterms: 
# -Inside the loop, print the value of n1, which represents the current term in the 
# Fibonacci sequence. 
# -Calculate the next term of the sequence by adding n1 and n2, and store it in the 
# variable nth. 
# -Update the values of n1 and n2: set n1 to n2 and n2 to nth. 
# -Increment the value of count by 1. 
# Step7. End the while loop. 
# Step8. End the program. 
# Source Code:

nterms = int(input("How many terms? ")) 
# first two terms 
n1, n2 = 0, 1 
count = 0 
# check if the number of terms is valid 
if nterms <= 0:
print(“ Please enter a positive integer”) 
# if there is only one term, return n1 
elif nterms == 1:
print("Fibonacci sequence upto",nterms,":")
print(n1) 
# generate fibonacci sequence 
else:
print("Fibonacci sequence:")
while count < nterms:
print(n1) 
nth = n1 + n2 
# update values 
n1 = n2 
n2=nth 
count +=1

# Output: 
# How many terms? 5 
# Fibonacci sequence: 
# 0
# 1
# 1
# 2
# 3 
