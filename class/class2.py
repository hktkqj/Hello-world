#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

class Movies() :
    def __init__(self,number) :
        self.name="Untitled"
        self.num=number
        self.rent=None
        self.bluray=None
        self.rentday=-1
        self.due=-1
        print("The number of this movie is "+str(self.num)+".")
        self.name=input("Please input the name of this movie :")
        self.type=int(input("Please input the type of the movie (1.Classic 2.Newly) :"))
        check=input("The movie is Blu-Ray version ? (Y/N) :")
        if check=="Y" :
            self.bluray=True
        else :
            self.bluray=False
        print("Successfully added",end="\n\n")

    def rent_movie(self,date):
        if not self.rent :
            choice=input("Rent "+self.name+" (No."+str(self.num)+") at "+str(date)+"day? (Y/N)")
            if choice=="Y" :
                self.rentday=date
                self.due=date+10
                self.rent=True
                print("Successfully rented, You should return it before "+str(self.due)+"th day.")
            elif choice=="N" :
                print("Cancelled")
        else :
            print(self.name+" (No."+self.num+") was rented on "+str(self.rentday)+"th day. It will be returned on "+str(retu)+"th day.",end="\n\n")

    def return_movie(self,date):
        if self.type==1 :
            price=2.25
        elif self.type==2 :
            price=4.95
        if self.bluray==True :
            price=price+1.5
        if date>self.due :
            price=price+(date-self.due)
            print("You are overdue! You should pay "+str(price)+" $ .")
        else :
            if data<self.rentday :
                print("Invaild return date.")
            else :
                print("You should pay " + str(price) + " $.")
        while True :
            paid=input("You paid:")
            if float(paid)<price :
                print("Paid failed,no enough money!")
                continue
            else :
                self.rent=False
                self.due=-1
                self.rentday=-1
                print("You have successfullt returned the movie!")
                break

class Shop() :
    def __init__(self):
        self.objlist={}
        self.num=0
        while True :
            os.system("cls")
            choice=input("Please input your choice:\n1.Add a movie\n2.Rent a movie\n3.Return a movie\n4.Show status\n")
            if choice=="1" :
                self.num = self.num + 1
                newmovie = Movies(self.num)
                self.objlist[self.num] = newmovie
                os.system("@pause")
				
            elif choice=="2" :
                number=int(input("Please input the number of Movie:"))
                date=int(input("Please input rent date:"))
                if number in self.objlist.keys() :
                    self.objlist[number].rent_movie(date)
                else :
                    print("No such movie!",end="\n\n")
                os.system("@pause")

            elif choice=="3" :
                number = int(input("Please input the number of Movie:"))
                if number in self.objlist.keys():
                    if self.objlist[number].rent == True :
                        date = int(input("Please input return date:"))
                        self.objlist[number].return_movie(date)
                    else :
                        print("You didn't rent this movie",end="\n\n")
                else :
                    print("No such movie!", end="\n\n")
                os.system("@pause")

            elif choice=="4" :
                print("Movie Infos: ")
                for num in self.objlist.keys() :
                    print(str(num)+"."+str(self.objlist[num].name),end="  Bluray:")
                    if self.objlist[num].bluray :
                        print("Yes",end="  Type:")
                    else :
                        print("No",end="  Type:")
                    if self.objlist[num].type==1 :
                        print("Classic",end="  Status:")
                    else :
                        print("New",end="  Status:")
                    if self.objlist[num].rent == True :
                        print("Rented  due:"+str(self.objlist[num].due),end="\n\n")
                    else :
                        print("Not rented",end="\n\n")
                os.system("@pause")

if __name__ == '__main__':
    a=Shop()
