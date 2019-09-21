#!/bin/python
#q1
'''
a=[]
for i in range(20,33):
	if(i%7==0) and (i%5!=0):
		a.append(i)
print(a)	


#q2

a=int(input("\nEnter a number"))
fac=1
for i in range (1,a+1):
	fac=fac*i
print("\nfac= ",fac)

#q3
d={}
for i in range (1,10):
        d[i]=i*i
print(d)
'''
#q4

li=[1,2,3,4]
tu=(1,2,3,4)
di={1:'a',2:'b'}
print("LIST:",li[0:2])
print("TUPLE:",tu[0:2])
print("DICTONARY:",di)
# reverse traversal
print("REVERSAL",li[-4:-2])




'''
#q5
class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print (self.s.upper())
strObj = InputOutString()
strObj.getString()
strObj.printString()

#q6

#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print (','.join(value))


#q7
ine = int(input())
dimensions=[int(x) for x in ine.split(',')]
row=dimensions[0]
col=dimensions[1]
multilist = [[0 for coln in range(col)] for rown in range(row)]
for rown in range(row):
    for coln in range(col):
        multilist[row][col]= row*col
print(multilist)'''

