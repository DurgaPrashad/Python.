# AIM: Write a program to compute summary statistics such as mean, median, 
# mode, standard deviation and variance of the given different types of data.
# Algorithm: 
# Import the necessary libraries: 
# import numpy as np from 
# scipy import stats 
# compute the mean: 
# mean = np.mean(data) 
# print("Mean:", mean) 
# compute the median: 
# median = np.median(data) 
# print("Median:", median) 
# compute the mode: 
# mode = stats.mode(data) 
# print("Mode:", mode.mode) compute the standard diviation: std_dev = 
# np.std(data) 
# print("Standard Deviation:", std_dev) 
# Source code: 

import numpy as np 
array = np.arange(10) 
print(array) 

# Output: 
# # [0 1 2 3 4 5 6 7 8 9] 
# # mean
r1 = np.mean(array) 
print("\nMean: ", r1) 
# Output 
# Mean: 4.5 
# median 
r2=np.median(array) 
print('\nmedian= ',r2) 
# Output 
# median= 4.5 
# mode 
import statistics 
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86] 
x = statistics.mode(speed) 
print('mode=',x) 
# Output 
# mode= 86 
# standard deviation 
r3 = np.std(array) 
print("\nstd: ", r3) 
# Output 
# std: 2.8722813232690143 
# variance 
r4 = np.var(array) 
print("\nvariance: ", r4) 
# Output 
# variance: 8.25
RESULT: program to compute summary statistics such as mean, median, 
mode, standard deviation and variance of the given different types of data 
Executed successfully
