#!/usr/bin/python
# -*- coding: UTF-8 -*-
def printlist() :
	str1=""
	for i in range(1,10) :
		for j in range(1,i+1) :
			str1=str1+str(j)+' * '+str(i)+'  ='+str(i*j)+'    '
		str1=str1+'\n'
	return str1

if __name__ == '__main__':
    print(printlist())