#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

def get_ten_popular_words(Filename) : 

	text=str(f.read())
	text=text.replace('\n', ' ')
	words=text.split(' ')
	Dict_Cnt={}
	for word in words :
		word=word.lower()
		if word in Dict_Cnt.keys() :
			Dict_Cnt[word]=Dict_Cnt[word]+1
		else :
			Dict_Cnt[word]=1
	result=""
	for num in range(0,10) :
		result=result+str(sorted(Dict_Cnt.items(),key=lambda d:d[1],reverse=True)[num][0])+':'+str(sorted(Dict_Cnt.items(),key=lambda d:d[1],reverse=True)[num][1])+' '
	return result

if __name__ == '__main__' :
	print(get_ten_popular_words("test.txt"))