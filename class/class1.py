#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
class Shape() :
    def area(self) :
        pass
    def perimiter(self):
        pass

class Rectrangle(Shape) :
    def __init__(self):
        self.length=int(input("Please input a length: "))
        self.width=int(input("Please input a width: "))
    def area(self):
        return self.length*self.width
    def perimiter(self):
        return 2*(self.length+self.width)

class Triangle(Shape) :
    def __init__(self):
        getlist = input("Please input length of each side: ").split(' ')
        self.l0 = int(getlist[0])
        self.l1 = int(getlist[1])
        self.l2 = int(getlist[2])
    def area(self):
        p=(self.l0+self.l1+self.l2)/2
        return (p*(p-self.l0)*(p-self.l1)*(p-self.l2)) ** 0.5
    def perimiter(self):
        return self.l0+self.l1+self.l2

class Circle(Shape) :
    def __init__(self):
        self.rad=int(input("Please input a radius: "))
    def area(self):
        return 2*math.pi*self.rad
    def perimiter(self):
        return math.pi*(self.rad**2)

if __name__ == '__main__':
    sp=Triangle()
    print(sp)