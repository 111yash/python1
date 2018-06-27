#Q.1- Name and handle the exception occured in the following program: 
#a=3
# if a<4:
#    a=a/(a-3)
#     print(a)
try:
	a=3
	if a<4:
		a=a/(a-3)
		print(a)
except Exception as e:
	print("Exception quard")
	print(a)
	print(e)
	
#Q.2- Name and handle the exception occurred in the following program: 
#l=[1,2,3]
#print(l[3])

try:
	l=[1,2,3]
	print(l[3])
except Exception as a:
	print(a)

#Q.3- What will be the output of the following code:
try:
	raise NameError("Hi there") 
except NameError :
    print("an exception")
	
#output	
an exception

#Q.4- What will be the output of the following code:
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output
-5.0
a/b result in 0


#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error

try:
	import Yash
except Exception as e:
	print(e)
	
#2. Value Error

try:
	y=int('ygytgfya')
except Exception as e:
	print(e)
#3. Index Error

l=[1,2,3]
	print(l[6])
except Exception as e:
	print(e)
	
 #Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. 
 #The code must keep taking input till the user enters the appropriate age number(less than 18).
 
class AgeTooSmallError(Exception):
	pass
while True:
		try:
			age =int(input("enter your age: "))
			if(age<19):
				raise AgeTooSmallError("age is too small: ")
			break
		except Exception as e:
				print(e)
				print(age)