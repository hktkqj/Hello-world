#!/usr/bin/python
# -*- coding: UTF-8 -*-

def d2b_b2d(Octnum, Binnum) :
#Check format
	Std_Oct_Set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ','}
	Std_Bin_Set = {'0', '1'}
	if set(str(Octnum))<=Std_Oct_Set and set(str(Binnum))<=Std_Bin_Set :
#Oct to Bin content
		result=[]
		while Octnum :
			result.append(Octnum % 2)
			Octnum=Octnum//2
		result.reverse()
		for num in result: print(num,end='')
		print(",",end='')
#Bin to Oct content
		now=1
		result1=0
		while Binnum :
			result1=result1+(Binnum % 10)*now
			now=now*2
			Binnum=Binnum//10
		print(result1)
	else :
		print("格式错误")
#EOD

if __name__ == '__main__':
	d2b_b2d(123,101001)