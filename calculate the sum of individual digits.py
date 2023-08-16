# Aim: write a python script calculate the sum of individual digits of a given 
# number.
# Algorithm:
# Step1. start 
# Step2. read the number 
# Step3. Sum=0 
# Step4. while number>0 
# Remainder- number%10 
# Sun-sum+ remainder 
# Number-number//10 
# Step5. dispiay result using print 
# Step6. End
# Source Code:

n=int(input('Enter any number: ')) 
num=n 
sum=0 
while n!=0: 
digit=n%10 
sum=sum+digit 
n=n//10 
print('Sum of Digit of ',num,'is: ',sum)

# Output:
# Enter any number: 456 
# Sum of Digit of 456 is: 15
# Result: Successfully completed to calculate sum of individual numbers.
