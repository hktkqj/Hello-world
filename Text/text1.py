#!/usr/bin/python
# -*- coding: UTF-8 -*-

def judge_if_parlindrome(Input_String) :
	Proc_Str=Input_String.replace(' ',"")
	list1=list(Proc_Str)
	list2=list1.copy()
	list1.reverse()
	if list1==list2 :
		return "The string" + " '" + Input_String + "' " + "is a palindrom"
	else :
		return "The string" + " '" + Input_String + "' " + "is not a palindrom"

if __name__ == '__main__':
	print(judge_if_parlindrome("abba"))