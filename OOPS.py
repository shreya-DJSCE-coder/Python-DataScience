class Student:
    subject="Python"
    college="ABC"
    year="4th  year"
    

a=10
stu1=Student()
stu2=Student()
print(type(stu1))
print(type(stu2))
print(stu1.subject)
print(stu1.college)
print(stu1.year)
print(stu2.subject)
# stu1.fun()
se=set()
print(type(se))
print(se)
s=set({})
print(type(s))
l=list()
print(l)
print(type(l))
lp=[]
print(type(lp))
print(lp)
#constructor
# constructor - > create or construct our objects
# init_method -> it is a special method which gets call every time when object is created. it initialises our object. basically if 
# we didnt wrote any init method in our class to python automatically wrote it and execute it 
# every time jb jb object create hota h tb tb init method call hota h. ye hmare object ko initialise krta h.

class Student_:
    course="Python"  #this are class attributes
    dob="1/2/2023"  #this are class attributes
    subj="Python"   #this are class attributes
    pass_year=2029
    # bcz the values of these attributes are common for all objects
    
    # constructor matlab -> hmara init method 
    def __init__(self,name,pg,cp):
        self.name1=name  #instance attribute
        self.age=pg  #instance attribute
        self.cgpa=cp  #instance attribute ->these can be differnt/common for all objects
        print("Constructor was called")
        print(f"{self.name1} is created")

    def get_cgpa(self):
        return self.cgpa  
      

stud1=Student_("Rahul",14,9.02)
stud2=Student_("Urvashi",18,8.44)
stud3=Student_("Shuyash",26,7.67)
print(stud1.name1)
print(stud1.dob)
print(stud1.age)
print(stud1.cgpa)
print(stud2.name1)
print(stud2.dob)
print(stud2.age)
print(stud2.cgpa)
print(stud3.name1)
print(stud3.dob)
print(stud3.age)
print(stud3.cgpa)

print(f"{stud1.get_cgpa()} is the cgpa of {stud1.name1} ")
print(f"{stud2.get_cgpa()} is the cgpa of {stud2.name1}")
print(f"{stud3.get_cgpa()} is the cgpa of {stud3.name1}")

# type of constructor
# 1. default constructor
# 2. parametarised constructor
 
# in c++, java ya other languages ek hi class me multiple constructor call kr skte h or compiler apne aap
# detect kr leta h like agar ek bhi parameter nhi h to us hisab se vo vala contructor call hoga agar 2 parameter h to us hisab 
# se jis constructor me 2 parameter h vo call hoga

# but in python it is not valid. in 1 class only one constuctor should be there

class Laptop:
    storage_type="ssd" # class attribute

    def __init__(self,a,b,c):
        self.RAM=a  #instance attribute
        self.storage=b
        self.model=c

    def get_info(self):  # instance method
        print(f"My model is {self.model}{"\n"}My RAM and storage is {self.RAM} and {self.storage}{"\n"}My storage type is {self.storage_type}")

    def gm(self):    # instance method
        print("Good Morning")

    @classmethod   #it is a decorator ise use krte h kisi bhi method ko class method bnane ke liye
                   #agar ise nhi likha to hm instance attribute ko bhi access kr payenge
    def getsto_type(cls):  # class method
        print(f"my storage type is {cls.storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        return final_price    


l1=Laptop("16gb","256gb","lenovo")
l2=Laptop("8gb","512gb","HP")
l3=Laptop("16gb","512gb","Dell")
l1.get_info()
l3.get_info()
l2.gm()
l3.gm()
l1.gm()
l1.getsto_type()
l2.getsto_type()
l3.getsto_type()
Laptop.getsto_type()

# jo bhi chije class ko mili h vo sbka access objects ko hota h but jo chije object ko mili hai unka sabka access class ko nhi hota h 

#instance method

# 1. 1st parameter - self
# 2.access the class attributes and instance attributes

#class method

# 1. 1st parameter - cls 
# 2. access only class attributes
# 3. decorator - @classmethod 

# static method

# 1.no compulsory parameter - no cls ,no self
# 2. access no instance attribute and no class attribute
# 3. decorator - @staticmethod

print(f" the final price of laptop 1 : {l1.calc_discount(12_000,34)}")
print(f" the final price of laptop 2 : {l2.calc_discount(30_000,20)}")

# OOPS Pillars 
# 1. Encapsulations -> capsule of two unit as a single unit
# 2. abstraction  
# 3. inheritance
# 4. polymorphism

# encapsulation :->  
# wrapping data and functions into single unit 
# same like capsule

# -> data hiding
# 1. public Data(attribute ) (accessible everywhere) by default
# 2. private Data(attribute) (accessible inside the class)
# 3. protected Data(attribute) (accessible in class and subclasses)

class BankAccount:
    def __init__(self,name,balance,accNo):
        self.name=name #public
        self._balance=balance  #protected  (convension not enforced)
        self.__accountNo=accNo  #private  (enforced)

    def getaccountNo(self):
        return self.__accountNo   

    def setaccountNo(self,ax):
        self.__accountNo=ax 
        
acc1=BankAccount("Rahul",12_000,"abAD230X")
print(acc1)
print(acc1.name)
print(acc1._balance)  # trick to access potected attribute
print(acc1.getaccountNo())   
# print(acc1.__accountNo) gives error bcz private attribute ko bahar access nhi kr skte h
# acc1.__accountNo="AS0Xc34R"  change nhi hoga means ye new value modify nhi hoga
acc1.setaccountNo("AS0Xc34R")
print(acc1.getaccountNo())
print(acc1._BankAccount__accountNo)  #trick to access private attribute
# since the attribute is protected or private but still we can access those that's why in python
# no one truly private or protected its just a convension that every developer should follow

# Inheritance
                # Employees  #parent class

# Teachers #child class    Administry #child class

# we recieve properties from our parents.whatever is of our parents that is also of their 
# children like home property
# surname,home,fan,food and other things


class Employee:
    start_time="10am"
    end_time="6pm"

    def change_endtime(self,entm):
        self.end_time=entm 

class Teacher(Employee):
    def __init__(self,salary,subject):
        self.salary=salary
        self.subject=subject

class Administry(Employee):
    def __init__(self,Role):
        self.role=Role

t1=Teacher(12_0000,"DBMS")
E1=Employee()
print(t1.salary)
print(t1.subject)
print(t1.start_time)
print(t1.end_time)   

a1=Administry("librarian")
print(a1.role)
print(a1.start_time)
print(a1.end_time)
                        
t1.start_time="12pm"
print(t1.start_time)
print(E1.start_time)
print(E1.end_time)
t1.change_endtime("11pm")
a1.change_endtime("9pm")
print(E1.end_time,t1.end_time,a1.end_time)

# Types of inheritance

# 1.Single level inheritance  : Parent -> child
# 2.multi level inheritance   : A1->B1->C1 
# 3.multiple inheritance      : A1+C1->B1
# 4.hirarchial inheritance   : A1->B1+C1+D1

#single level inheritance

class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class child(Parent):
    def __init__(self,name,edu,age,clg):
        super().__init__(name,age)
        self.edu=edu
        self.clg=clg

C1=child("Romil","12th",19,"DJSCE") 
P1=Parent("Shambhu",45) 
print(C1.name,C1.age,C1.edu,C1.clg)
print(P1.name,P1.age)      

#multi level inheritance

class building:
    NoFloor=6
    def __init__(self,height,yom):
        self.height=height
        self.yom=yom

class College(building):
    def __init__(self,course,years,dept,height,yom):
        self.course=course
        self.year=years
        self.nodept=dept
        super().__init__(height,yom)

class School(College):
    def __init__(self,uniform_col,course,years,dept,height,yom):
        self.uniform_col=uniform_col
        super().__init__(course,years,dept,height,yom)


b1=building("12km",25)
c1=College("Btech",4,4,"15km",50)
s1=School("blue","academic",12,2,"5km",20)
print(b1.height,b1.yom,b1.NoFloor)
print(c1.course,c1.year,c1.nodept,c1.height,c1.yom,c1.NoFloor)
print(s1.uniform_col,s1.course,s1.year,s1.nodept,s1.height,s1.yom,s1.NoFloor)

#multiple inheritance

class Teacher:
    def __init__(self,salary):
        self.salary=salary

    def get_info_teacher(self):
        print(self.salary)    

class Student:
    def __init__(self,fees,gpa):
        self.fees=fees
        self.gpa=gpa

    def get_info_stu(self):
        print(self.fees,self.gpa)
        
class TA(Teacher,Student):
    def __init__(self, salary,fees,gpa,timing):
        self.timing=timing
        Teacher.__init__(self,salary)
        Student.__init__(self,fees,gpa)

    def getinfo_TA(self): 
        print(self.timing)
        super().get_info_teacher()
        super().get_info_stu()   

t1=Teacher(10_000)
s1=Student(2_30_0000,9.33)
ta1=TA(12_000,1_90_000,8.5,"afternoon shift")
t1.get_info_teacher()
s1.get_info_stu()
ta1.getinfo_TA()

#hirarchiel inheritance

class goods:
    def __init__(self,price,variety):
        self.price=price
        self.variety=variety

class Fruits(goods):
    def __init__(self,ftype,price, variety):
        self.ftype=ftype
        super().__init__(price, variety)        

class Veg(goods):
    def __init__(self,vtype,price, variety):
        self.vtype=vtype
        super().__init__(price, variety)

g1=goods(120,"A")
f1=Fruits("Apple",150,"A3")
v1=Veg("Potato",100,"B1")
print("I am good :",g1.price,g1.variety)
print("I am fruit : ",f1.ftype,f1.price,f1.variety)
print("I am vegetable : ",v1.vtype,v1.price,v1.variety)

#something interesting

class M:
    name="rohan"
    age="34"
    def __init__(self,yu):
        self.yoe=yu

class N:
    def __init__(self,edu,yu):
        self.edu=edu
        M.__init__(self,yu)

m1=M(10)
n1=N("BSC",18)
print("I am M : ",m1.yoe)
print("I am N : ",n1.yoe,n1.edu)

#abstraction
# Hiding internal details & showing only essencial features

# for example we use multiple apps like the most populer is chatgpt where we only see the outputs.
# the internal work means the background things means what is happening inside is completely hidden for us.

#abc module se ABC -> Abstract based classes import kra and then abstractmethod which is a decorator import kra.
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo")

l1=Lion()
c1=Cow()
l1.make_sound()
c1.make_sound()
       
#


                 





        
 




                        

        
    
        

                
        


            




        
