# Aim: Write a python script to find the largest number among three numbers and 
# display them in ascending order using if-else construct.
# Algorithm: 
# Step1. Start the program. 
# Step2. Prompt the user to enter the first number and store it in the variable a. 
# Step3. Prompt the user to enter the second number and store it in the variable b. 
# Step4. Prompt the user to enter the third number and store it in the variable c. 
# Step5. Compare a, b, and c to find the largest number using if-else constructs: 
# - If a is greater than both b and c, set the variable largest to a. 
# -If b is greater than both a and c, set the variable largest to b. 
# -Otherwise, set the variable largest to c. 
# Step6. Compare a, b, and c to find the smallest number using if-else constructs: 
# - If a is smaller than both b and c, set the variable smallest to a. 
# -if b is smaller than both a and c, set the variable smallest to b. 
# -Otherwise, set the variable smallest to c. 
# Step7. Calculate the middle number by subtracting the sum of largest and 
# smallest from the sum of a, b, and c, and store it in the variable mid. 
# Step8. Print the largest number with the message "largest number: " followed 
# by the value of the variable largest. 
# Step9. Print the message "Ascending order". 
# Step10. Print the smallest, mid, and largest numbers in ascending order using 
# the print statement: 
# print(smallest, mid, largest). 
# Step11. End the program.
# Source Code:

a=int(input('Enter the first number: ')) 
b=int(input('Enter the second number: ')) 
c=int(input('Enter the third number: '))
if a>b and a>c:
largest=a 
elif b>a and b>c:
largest=b 
else:
largest=c 
if a<b and a<c:
smallest=a 
elif b<a and b<c:
smallest=b 
else:
smallest=c 
mid=(a+b+c)-(largest+smallest) 
print('largest number: ',largest) 
print('Ascending order.........') 
print(smallest,mid,largest)

# Output:
# Enter the first number: 10 
# Enter the second number: 12 
# Enter the third number: 14 
# largest number: 14 
# Ascending order......... 
# 10 12 14
# Result:
# To find the largest of three numbers and display them in ascending order 
# using ifelse construct executed successfully
