#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fibonacci_recursion(Time) :
	Std_Set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
	if set(str(Time)) <= Std_Set:
		if Time == 1 or Time == 2 :
			return 1;
		else :
			return fibonacci_recursion(Time-1)+fibonacci_recursion(Time-2);
	else :
		print("参数异常")

def fibonacci_loop(Time) :
	Std_Set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',}
	if set(str(Time))<=Std_Set :
		Seq=[1,1]
		if Time == 1 or Time == 2 :
			return 1;
		else :
			for num in range(1,Time-1) :
				Seq.append(Seq[-1]+Seq[-2])
		return Seq[-1]
	else :
		print("参数异常")

if __name__ == '__main__':
	print('Recursion result : ',fibonacci_recursion(11))
	print('Loop result : ',fibonacci_loop(11))
			