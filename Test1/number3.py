#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

def haversine_formula(lon1,lat1,lon2,lat2) :
	if (lon1>180) or (lat1>90) or (lat2>90) or (lon1>180) :
		return ("格式错误")
	else :
		C = math.sin((lat1*math.pi)/180)*math.sin((lat2*math.pi)/180)+math.cos(((lon1-lon2)*math.pi)/180)*math.cos((lat1*math.pi)/180)*math	.cos((lat2*math.pi)/180)
		return 6371.004*math.acos(C)

if __name__ == '__main__' :
	print(haversine_formula(112.3,25.3,152.6,36.4))