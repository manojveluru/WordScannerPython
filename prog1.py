#!/usr/bin/python3
"""
						CSCI 503 - Assignment 1 - Spring 2019
						Progammer: Manoj Veluru
						Z-ID: Z1840907
						Section: 1
						Date Due: February 7, 2019
						Purpose: write and implement a Python program to
						compute the statistical values from a given list of floating-point numbers.
a good program
"""
import sys

"""Method to read floating point numbers from stdin and storing them in empty list"""
def read_data(numbers):
	for line in sys.stdin:
		line = line.strip()
		numbers.append(float(line))
	
'''Method to calculate and return computed standard deviation'''
def std_deviation(numbers,mean):	
	if len(numbers) >1:
		std_dev = (sum([(n - mean)**2 for n in numbers])/(len(numbers)-1))**0.5
	else:
		std_dev = format(0.0, '.2f')
	return std_dev 
	

'''Method to print the computed statistical values '''
def print_stat():
	numbers = [] #Empty list
	read_data(numbers)  #Function call to read input numbers
	print("\nOutput Statistics for Input Data")
	print("--------------------------------")
	if len(numbers) >= 1:
		lowest_num = '%10s' % (round((min(numbers)),2)) #Rounding off to 2 decimal points and right aligned
		highest_num = '%9s' % (round((max(numbers)),2))
		total_sum = sum(numbers)
		mean = '%9s' % (round(total_sum/len(numbers),2)) #Mean Calculation
		print("Low:" +lowest_num)
		print("High:"+highest_num)
		print("Mean:"+str(mean))
		if len(numbers) >1:
			std_deviation1 = '%7s' % (round(std_deviation(numbers,float(mean)),2)) #Function call to get standard deviation
			print("StdDev:"+str(std_deviation1))
		else:
			std_deviation2 = '%7s' % (std_deviation(numbers,mean))
			print("StdDev:"+str(std_deviation2))
	else:																				#Just printing labels if there are no statistical values 
		print("Low:")
		print("High:")
		print("Mean:")
		print("StdDev:")
	

print_stat() #Function Calling
	
	
