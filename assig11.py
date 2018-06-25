#create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
from threading import Thread
import time

def display():
 print("wait for 2 seconds\n")
 time.sleep(2)
 print("Hey Yash Nainiwal")

t=Thread(target= display)
t.setName("hello python")
t.start()


print("\n************************\n") 


#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between
import threading
from threading import Thread
import time
def display(num):
	for x in range(num):
		print(x)
		time.sleep(5)
num= 10
t=Thread(target=display,args=(num,))
t.start()

 #Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display. Delay goes like 2sec-4sec-6sec-8sec-10sec
import threading
from threading import Thread
import time
def display():
	l=[1,2,3,4,5]
	for x in l:
		print(x)
		time.sleep(2)
  
  
t=Thread(target=display)
t.start()
  
print("\n********************************\n")

  #Q4. Call factorial function using thread.
import threading
from threading import Thread
import time
import math 
def factorial(num):
	print("wait 1 seconds for result")
	time.sleep(2)
	print("facorial is:",math.factorial(num))
	
num=int(input("enter any no. to find factorial\n"))
t=Thread(target=factorial(num))
t.start()