# Aim: To get the difference between the two lists. 
# iv. To get the difference between the two lists. 
# Algorithm: 
# 1.Start the program. 
# 2.Create two lists, list1 and list2, which represent the two lists you want to find 
# the difference between. 
# 3.Create an empty list named "difference" to store the elements that are present 
# in list1 but not in list2. 
# 4.Iterate through each element in list1 using a for loop: 
# -Inside the loop, check if the current element is present in list2 using the "in" 
# operator. 
# -If the current element is not present in list2, append it to the "difference" list. 
# 5.After the loop, the "difference" list will contain the elements that are present 
# in list1 but not in list2. 
# 6.Print the "difference" list to display the difference between the two lists. 
# 7.End the program. 
# Source code: 

list1=[50,12,48,76,25] 
list2=[25,30,17,96,12] 
list3=[] 
for i in range(len(list1)): 
list3.append(list1[i]-list2[i]) 
print('Difference of',list1,'and',list2,'=',list3) 

# Output: Difference of [50, 12, 48, 76, 25] and [25, 30, 17, 96, 12] = [25, -18, 
# 31, - 20, 13] 
# Result: To get the difference between the two lists is successfully executed
