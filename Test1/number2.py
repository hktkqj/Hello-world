#!/usr/bin/python
# -*- coding: UTF-8 -*-

def get_changes(goods,pay) :
#Price List:
	Item_Price={
		"item01" : 2.3,
		"item02" : 35.8,
		"item03" : 16.3,
		"item04" : 12,
		"item05" : 13.6,
		"item06" : 29,
		"item07" : 17.4,
		"item08" : 63.9,
		"item09" : 56.7,
		"item10" : 23.8
		}
	Changes={50:0,20:0,10:0,5:0,1:0,0.5:0,0.1:0}
	if goods in Item_Price.keys() :
		if pay < Item_Price[goods] :
			print("支付金额不足,请重新支付...")
		else :
			Temp_Remain=pay-Item_Price[goods]
			for num in Changes.keys() :
				while Temp_Remain>=num :
					Temp_Remain=Temp_Remain-num
					Changes[num]=Changes[num]+1
				if num==0.1 :
					print(str(num) + '*' + str(Changes[num]))
				else :
					print(str(num) + '*' + str(Changes[num]),end=',')
	else :
		print("无此商品,请重新选择...")
#End Of Function

if __name__ == '__main__':
    get_changes("item01",6)
