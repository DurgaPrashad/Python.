AIM: Write a script named copyfile.py. This script should prompt the user for 
the names of two text files. The contents of the first file should be the input that 
to be written to the second file. 
# Algorithm: 
# Step 1: Prompt the user to enter the name of the source file (the file to be 
# copied). 
# Step 2: Read the input from the user and store it in a variable. 
# Step 3: Prompt the user to enter the name of the destination file (the file to copy 
# the contents to). 
# Step 4: Read the input from the user and store it in another variable. 
# Step 5: Open the source file in read mode using the open() function. 
# Step 6: Read the contents of the source file using the read() method and store it 
# in a variable. 
# Step 7: Open the destination file in write mode using the open() function. 
# Step 8: Write the contents of the source file to the destination file using the 
# write() method. 
# Step 9: Close both the source and destination files. 
# Step 10: Display a message to the user indicating that the file has been 
# successfully copied. 
# Source code: 
# to prompt the user to enter the file1 which is input file 
infile=input("enter the input filename with extension ") 
# to prompt the user to enter the file2 which is output file 
outfile=input("enter the output filename with extension ") 
#opening the file1 in reading mode 
f1=open(infile,"r") 
#opening the file2 in output mode 
f2=open(outfile,"w+") 
#reading the content of file1 to content variable 
content=f1.read() 
#writing to the value of content variable to 
file2 f2.write(content) 
#closing the file1 and file2 
f1.close() 
f2.close() 
Output: 
1. Create file4.txt and copy the below content 
Messi is the best footballer in the world. 
He plays for Argentina. 
2. Run the program enter the input filename with extension file4.txt enter the 
output filename with extension file5.txt 
3. Content of file5.txt 
Messi is the best footballer in the world. 
He plays for Argentina. 
RESULT: script named copyfile.py. This script should prompt the user for the 
names of two text files. The contents of the first file should be the input that to 
be written to the second file executed successfully
