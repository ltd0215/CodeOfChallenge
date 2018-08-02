#!/usr/bin/env python3

import sys

try:
	for arg in sys.argv[1:]:
		origin = int(arg.split(':')[1])
		insurance = origin * 0.165
		Ying = origin - insurance - 3500
		if Ying <=1500:
			tax = Ying * 0.03 - 0
		elif Ying > 1500 and Ying <= 4500:
			tax = Ying * 0.10 - 105
		elif Ying > 4500 and Ying <= 9000:
			tax = Ying * 0.20 - 555
		elif Ying > 9000 and Ying <= 35000:
			tax = Ying * 0.25 - 1005
		elif Ying > 35000 and Ying <= 55000:
			tax = Ying * 0.30 - 2755
		elif Ying > 55000 and Ying <= 80000:
			tax = Ying * 0.35 - 5505
		else:
			tax = Ying * 0.45 - 13505
		if tax < 0:
			tax = 0
		salary = origin - insurance - tax
		print('{}:{:.2f}'.format(arg.split(':')[0], salary))
except: 
	print("Parameter Error")

