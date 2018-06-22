#Create a Circle Class and Initialize it with Radius.
class Circle:
	def __init__(self,radius):
		self.r=radius
		
	def getArea(self):
		print(self.r*self.r*3.14)
		
	def getCircumference(self):
		print(self.r*2*3.14)
		
c =Circle(2)

c.getArea()
c.getCircumference() 

#Create a Student Class and make Display And SetAge Method
class Student:
	def __init__(self,name,rollno):
		self.info=name
		self.n=rollno
	def show(self):
		print(self.info,self.n)
x=(input("enter name:"))
y=int(input("enter rollno:"))
s=Student(x,y)
s.show()
#Create a Temperature class. Make two Methods
class Temperature:
	def __init__(self,celsius,fahrenheite):
		self.n=celsius
		self.m=fahrenheite
	def show(self):
		print((self.n+32)*1.8)
		print((self.m-32)/1.8)
x=int(input("enter celsius"))
y=int(input("enter fahrenheite:"))
s=Temperature(x,y)
s.show()

#Create a Temperature class. Make two Methods
class MovieDetails:
	def __init__(self,name,artisname,yearofrelease,rating):
		self.l=name
		self.n=artisname
		self.m=yearofrelease
		self.o=rating
	def show(self):
		print(self.l,self.n,self.m,self.o)
	def update(self,name,artisname,yearofrelease,rating):
		self.l=name
		self.n=artisname
		self.m=yearofrelease
		self.o=rating
s2=MovieDetails("deadpool","ryan reynolds",2018,"9out of 10")
s2.show()
s2.update("transpoter","jason satham",2016,"8out of 10")
s2.show()

#Create a Expenditure class.And Initialize it
class expendicture:
	def __init__(self,expendicture,saving):
		self.e=expendicture
		self.s=saving
	def show(self):
		print(self.e,self.s)
	def add(self):
		total_salary=(self.e+self.s)
		print(total_salary)
x=int(input("enter expendicture spend:"))
y=int(input("enter saving:"))
s=expendicture(x,y)
s.show()
s.add()

#Create a Class Cope and Initialize it 
class cop:
	def __init__(self,name,age,workexperience and designation):
		self.n=name
		self.a=age
		self.we=workexperience
		self.d=designation
	def show(self):
		print(self.n+self.a+self.we+self.d)
	def update(self,name,age,workexperience,designation):
		self.n=name
		self,a=age
		self.we=workexperience
		self.d=designation
d=cop("serv",23,"2 years","officer")
d.show
d.update("jason",31,"21 years","ips")
