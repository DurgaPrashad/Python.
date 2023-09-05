# AIM: Write a Python program to count the number of characters (character 
# frequency) in a string. 
# Algorithm: 
# Step 1: Initialize an empty dictionary to store the character frequencies. 
# Step 2: Prompt the user to enter a string. 
# Step 3: Use a loop to iterate through each character in the string. 
# -Within the loop, check if the character is already present in the dictionary. 
# -If yes, increment the count of that character by 1. 
# -If no, add the character to the dictionary with a count of 1. 
# Step 4: Display the character frequencies. 
# Source code: 

Sample String: google.com' 
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1} 
word=input('Enter any string: ') 
print(word) 
char_freq={} 
for i in word: 
if i not in char_freq: 
char_freq[i]=1 
else: 
char_freq[i]+=1 
print(char_freq) 


# Output: 
# google 
# {'g': 2, 'o': 2, 'l': 1, 'e': 1} 
# RESULT: Write a Python program to count the number of characters (character 
# frequency) in a string executed successfully.
