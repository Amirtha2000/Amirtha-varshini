#!/bin/python
import re
fl2=fl3=fl1=f=0
s=input("Enter a password to check for validity")
if not s.__len__()>6 and s.__len__()<12:
    print("not valid no. of characters")
for i in s:
      if  i>='a' and i<='z':
          fl1+=1
      elif i>='A' and i<='Z':
          fl2+=1
      elif  i>= '0' and i<='9':
          fl3+=1
      else:
          f+=1
if fl1==0:
    print("missing small character")
elif fl2==0:
    print("missing Upper character")
elif fl3==0:
    print("missing number")
elif f==0:
    print("Special character missing")
else:
   print("Valid password")


