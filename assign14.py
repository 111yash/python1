#Q.1- Write a Python program to read last n lines of a file
c = -1
f=open('new 1.txt','r')
content=f.readlines()
n=int(input("enter the number of line: "))
while c >= -n:
	print(content[c],end="")
	c= c - 1
f.close()

#file=new 1.txt
Hello world!
Hello python!
Hello java!
Hello html!
Hello keshav
Hello yash
Hello vibhor


#Q.2- Write a Python program to count the frequency of words in a file.

with open('new 1.txt','r') as f:
	content = f.read()

words = content.split()

s = set(words)


for n in s:
	print(n,words.count(n))

file=new 1.txt

Hello world!
Hello python!
Hello java!
Hello html!
keshav
yash 
vibhor 
gurukirat

#Q.3- Write a Python program to copy the contents of a file to another file

with open("new 1.txt") as f:
    with open("new 2.txt", "w") as f1:
        for line in f:
            f1.write(line)
			
#first file=new 1.txt
keshav 
yash 
vibhor
gurukirat

#second file=new 2..txt
keshav
yash
vibhor
gurukirat

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
with open('new 1.txt') as f1:
	with open('new 2.txt') as f2:
		for line1,line2 in zip(f1, f2):
			print(line1+line2)
v			
file=new 1.txt
hello world
file=new 2.txt
hello keshav

#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

import random
def Rand(start, end, num):
	res = []

	for j in range(num):
		res.append(random.randint(start, end))

	return res
num = 10
start = 20
end = 40
res = Rand(start, end, num)
f=open('new 2.txt','w')
for n in res:
	f.write(str(n))
	f.write("\n")
f.close()	

f = open('new 2.txt','r')
l = f.readlines()
f.close()
l.sort()

f = open('new 3.txt','w')
for n in l:
	f.write(n)
	f.write("\n")
	
f.close()
