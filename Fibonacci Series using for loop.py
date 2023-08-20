# #Fibonacci Series using for loop
# Algorithm:
# Step1. Start the program. 
# Step2. Prompt the user to enter the number of terms they want in the Fibonacci 
# sequence and store it in the variable nterms. 
# Step3. Initialize the variables n1 and n2 to 0 and 1, respectively, which 
# represent the first two terms of the Fibonacci sequence. 
# Step4. Print the message "Fibonacci sequence:". 
# Step5. Use a for loop that iterates over the range from 0 to nterms: 
# -Inside the loop, print the value of n1, which represents the current term in the 
# Fibonacci sequence. 
# -Calculate the next term of the sequence by adding n1 and n2, and store it in the 
# variable nth. 
# -Update the values of n1 and n2: set n1 to n2 and n2 to nth. 
# Step6. End the for loop. 
# Step7. End the program. 
# Source Code:


nterms = int(input("How many terms? ")) 
# first two terms 
n1, n2 = 0, 1 
count = 0 
# check if the number of terms is valid 
if nterms <= 0:
print("Please enter a positive integer") 
# if there is only one term, return n1 
elif nterms == 1:
print("Fibonacci sequence upto",nterms,":")
print(n1) 
# generate fibonacci sequence 
else:
print("Fibonacci sequence:")
for count in range(nterms):
print(n1) 
nth = n1 + n2 
# update values 
n1 = n2 
n2 = nth 
count += 1


# Output:
# How many terms? 6 
# Fibonacci sequence: 
# 0
# 1
# 1
# 2
# 3
# 4
# 5
#result
#Python script to display Fibonacci sequence of numbers executed 
#successfully
