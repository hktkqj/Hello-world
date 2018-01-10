#!/usr/bin/python
# -*- coding: UTF-8 -*-
def is_leap_year(year) :
	if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0) :
		return True
	else :
		return False

def get_num_of_days_in_month(year, month) : 
	day={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
	if is_leap_year(year) :	
		day[2]=29
	return day[month]

def get_total_num_of_day(year, month): 
	start=0
	for y in range(1900,year) :
		if is_leap_year(y) :
			start=start+366
		else :
			start=start+365
	for m in range(1,month) :
		start=start+get_num_of_days_in_month(year,m)
	return start

def get_start_day(year, month) :
	return (get_total_num_of_day(year, month)+1) % 7

def calender(year,month) :
	Std_Oct_Set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ','}
	if not ( set(str(year)) <= Std_Oct_Set  and set(str(month)) <= Std_Oct_Set ) :
		return  "参数异常"
	if year<1900 or year>2100 or month<=0 or month>12 :
		return "日期有误"
	ori="Mon Tue Wed Thu Fri Sat Sun\n"
	dict={1:'  1 ',2:'  2 ',3:'  3 ',4:'  4 ',5:'  5 ',6:'  6 ',7:'  7 ',8:'  8 ',9:'  9 ',\
		 10:' 10 ',11:' 11 ',12:' 12 ',13:' 13 ',14:' 14 ',15:' 15 ',16:' 16 ',17:' 17 ',18:' 18 ',\
		 19:' 19 ',20:' 20 ',21:' 21 ',22:' 22 ',23:' 23 ',24:' 24 ',25:' 25 ',26:' 26 ',27:' 27 ',28:' 28 ',29:' 29 ',30:' 30 ',31:' 31 '}
	sd=get_start_day(year, month)
	for sn in range(1,sd) :
		ori=ori+"    "
	for day in range(1,get_num_of_days_in_month(year, month)+1) :
		if sd % 7 == 0 :
			ori=ori+dict[day]+'\n'
		else :
			ori=ori+dict[day]
		sd=sd+1
	return ori

if __name__ == '__main__':
	print(calender(2011,12))