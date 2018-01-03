#!/usr/bin/python
# -*- coding: UTF-8 -*-
def move(f,s):
	print(f + " -> " + s)
def Hanoi(n,a,b,c):
	if n==1 :
		move(a,c)
	else :
		Hanoi(n-1,a,c,b)
		move(a,c)
		Hanoi(n-1,b,a,c)
Hanoi(3,'A','B','C')