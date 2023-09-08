AIM: Write a program that inputs a text file .the program should print all of the 
 unique words in the file in alphabetical order 

# Algorithm: 
# Step 1: Prompt the user to enter the file name or path. 
# Step 2: Read the input from the user and store it in a variable. 
# Step 3: Open the file using the open() function in read mode. 
# Step 4: Read the contents of the file using the read() method and store it in a 
# variable. 
# Step 5: Split the contents into individual words using the split() method. 
# Step 6: Create an empty set to store the unique words. 
# Step 7: Iterate through each word in the list of words. 
# -Add each word to the set, as sets automatically discard duplicates. 
# Step 8: Convert the set of unique words to a list. 
# Step 9: Sort the list of unique words in alphabetical order using the sort() 
# method. 
# Step 10: Iterate through each word in the sorted list. 
# -Print each word. 
# Step 11: Close the file. 
# Source code: 
f1=open('file1.txt','r') 
f3=open('file3.txt','w') 
text=f1.read() 
# print(text) 
text=text.lower() 
words=text.split() 
# print(words) 
for word in words:
word.strip(',;!.()[] ') 
words=[word.strip(',;!.()[] ') for word in words] 
words=[word.replace("'s",'') for word in words] 
# finding unique 
unique=[] 
for word in words: 
if word not in unique: 
unique.append(word) 
unique.sort() 
for word in unique: 
f3.write('\n') 
f3.write(word) 
f1.close() 
f3.close() 
# Output: 
# Note:-Open file1.txt in the same path of the program and copy the content 
# given below 
# File1.txt content 
# Python is an interpreted high-level general-purpose programming language. Its 
# design philosophy emphasizes code readability with its use of significant 
# indentation. 
# File3.txt content 
# an
# code 
# design 
# emphasizes 
# general-purpose
# high-level 
# indentation 
# interpreted 
# is 
# its 
# language 
# of 
# philosophy 
# programming 
# python 
# readability 
# significant 
# use 
# with 
Result: program that inputs a text file .the program should print all of the 
unique words in the file in alphabetical order Executed successfully
