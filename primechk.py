#!/bin/python
a=int(input("Enter a number efor prime check"))
fac=0
for i in range(1,a-1):
	if(a%i==0):
 		 fac=1;
if(fac==0):
	print("ITS A PRIME")
