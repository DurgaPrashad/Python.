# Aim: To find the list of words are longer than n from a given list of words. 
# iii. To find the list of words that are longer than n from a given list of 
# words. 
# Algorithm: 
# 1.Start the program. 
# 2.Create a list of words and store it in a variable named "words". 
# 3.Prompt the user to enter the minimum length (limit) and store it in a variable 
# named "limit". 
# 4.Create an empty list named "new_words" to store the words longer than the 
# limit. 
# 5.Iterate through each word in the "words" list using a for loop: 
# -Inside the loop, check the length of the current word using the len() function. 
# -If the length of the current word is greater than the limit, go to the next step. 
# Otherwise, skip to the next word. 
# -Append the current word to the "new_words" list. 
# 6.After the loop, the "new_words" list will contain all the words longer than the 
# limit from the "words" list. 
# 7.Print the "new_words" list to display the list of words longer than the limit. 
# 8.End the program. 
# Source code: 

words=['rose','lily','jasmine','tulip','sunflower','daffodil','aster','pansy'] 
limit=int(input('Enter the length: ')) 
new_words=[] 
for word in words: 
 if len(word)>limit: 
 new_words.append(word) 
print(new_words) 

# Output:
# Enter the length: 4 
# ['jasmine', 'tulip', 'sunflower', 'daffodil', 'aster', 'pansy'] 
# RESULT: 
# The list of words are longer than n from a given list of words successfully 
# executed.
