#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fibonacci_recursion(Time) :
	if Time == 1 or Time == 2 :
		return 1;
	else :
		return fibonacci_recursion(Time-1)+fibonacci_recursion(Time-2);
	


def fibonacci_loop(Time) :
	Seq=[1,1]
	if Time == 1 or Time == 2 :
		return 1;
	else :
		for num in range(1,Time-1) :
			Seq.append(Seq[-1]+Seq[-2])
	return Seq[-1]

if __name__ == '__main__':
	Input_Data = input("Please input numbers:")
	NumSet = set(Input_Data)
	Std_Set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ','}
	if NumSet <= Std_Set:
		rec = int(Input_Data.split(',', 1)[0])
		loop = int(Input_Data.split(',', 1)[1])
	else:
		print("参数异常")
	print('Recursion result : ',fibonacci_recursion(rec))
	print('Loop result : ',fibonacci_loop(loop))
			