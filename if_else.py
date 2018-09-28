#!/bin/python3

N = int(input())

result = N % 2
if result == 1:
	print("Weird")
else: 
	if N>20:
		print("Not Weird")
	else:    
		if N>=6:
			print("Weird")
		else:
			print("Not Weird")