#!/bin/python

# login part
user="admin"
pswrd="123"
luser= input("Enter the user name:")
lpswrd=input("Password:")
if(user==luser):
	if(pswrd==lpswrd):
		print("WELCOME ADMIN")
	else:
		print("Enter the correct password:")
         