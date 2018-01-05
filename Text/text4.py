#!/usr/bin/python
# -*- coding: UTF-8 -*-

def get_ten_popular_words(Filename) : 
	f=open(Filename)
	text=str(f.read())
	text=text.replace(',','')
	text=text.replace('.', '')
	text=text.replace('!', '')
	text=text.replace('?', '')
	text=text.replace('\n', '')
	words=text.split(' ')
	Dict_Cnt={}
	for word in words :
		if word in Dict_Cnt.keys() :
			Dict_Cnt[word]=Dict_Cnt[word]+1
		else :
			Dict_Cnt[word]=1
	for num in range(0,10) :
		print(str(sorted(Dict_Cnt.items(),key=lambda d:d[1],reverse=True)[num][0])+':'+str(sorted(Dict_Cnt.items(),key=lambda d:d[1],reverse=True)[num][1]),end=' ')

if __name__ == '__main__' :
	get_ten_popular_words("test.txt")