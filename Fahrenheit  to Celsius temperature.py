# AIM: Write a python script to convert the following using functions Fahrenheit 
# to Celsius temperature and Celsius to Fahrenheit temperature. 
# Algorithm: 
# Fahrenheit to Celsius Conversion: 
# Step 1: Define a function fahrenheit_to_celsius(fahrenheit) that takes a 
# temperature in Fahrenheit as input. 
# Step 2: Calculate the temperature in Celsius using the formula: celsius = 
# (fahrenheit - 32) * 5/9. 
# Step 3: Return the temperature in Celsius. 
# Celsius to Fahrenheit: 
# Step 1: Define a function celsius_to_fahrenheit(celsius) that takes a temperature 
# in Celsius as input. 
# Step 2: Calculate the temperature in Fahrenheit using the formula: fahrenheit = 
# (celsius * 9/5) + 32. 
# Step 3: Return the temperature in Fahrenheit. 
# Source code: 
def tempConverter(choice): 
if choice==1: 
celsius=5*(temp-32)/9 
print('The temperature in Celsius',celsius) 
else: 
fahrenhite=(9*temp/5)+32 
print('The temperature in Fahrenhite',fahrenhite)
print('Enter the choice') 
print('1. Convert Fahrenhite to celsius') 
print('2. Convert Celsius to Fahrenhite') 
choice=int(input('Enter your choice: ')) 
temp=float(input('Enter the temperature: ')) 
tempConverter(choice) 
Output: 
# Enter the choice 
# 1. Convert Fahrenhite to celsius 
# 2. Convert Celsius to Fahrenhite 
# Enter your choice: 1 
# Enter the temperature: 212 
# The temperature in Celsius 100.0 
# RESULT: python script to convert the following using functions Fahrenheit to 
# Celsius temperature and Celsius to Fahrenheit temperature. Executed 
# successfully
