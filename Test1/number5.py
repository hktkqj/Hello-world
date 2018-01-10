#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

def is_palin(num_int): 
	list1=list(str(num_int))
	list2=list1.copy()
	list2.reverse()
	if list1==list2 :
		return True
	else :
		return False

def is_prime(num_int):
	if num_int == 2 :
		return True
	square_num = math.floor( num_int ** 0.5 )
	for i in range(2, (square_num+1) ): 
		if (num_int % i) == 0:
			return False
	return True
	
def get_num_factorial(num_int) :
	tot=1
	for i in range(1,num_int+1) :
			tot=tot * i
	std_set=set(['0','1','2','3','4','5','6','7','8','9'])
	if set(list(str(num_int))) <= std_set :
		if (is_palin(num_int) and is_prime(num_int)) :
			return str(num_int)+','+str(tot)
		else :
			return "非回文或者非素数"
	else :
		return "参数异常"

if __name__ == '__main__':
	print(get_num_factorial(101))