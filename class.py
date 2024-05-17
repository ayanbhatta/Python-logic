'''instan method acts upon the instance variable of class
instant method are of two type
1.accessor 
2. mutator

Class method

'''
class Bird:
    wings=2
    @classmethod
    def fly(self,x):
        print(f"{x} will hve {self.wings} wings")
# Bird.fly("Sparrow")
# Bird.fly("Parrot")


'''static method'''
class MyClass:
    n=0
    def __init__(self):
        MyClass.n=MyClass.n+1
        
    def NoObj():   #static method
        print("No of objrct ",MyClass.n)
ob1=MyClass()
ob2=MyClass()
ob3=MyClass()
#MyClass.NoObj()

'''INNER CLASS
enested class is a defined entirely within the body of another class
if an object is created, the obj inside the root class can be used


Kinds of relationships
1. Instantiating r (OOP allows r btw class and instance of the class)
2. Utilization r (OOP allows class to make use of another class)
3. Composition r (OOP allows you ti form an object, which includes another object as an part)
4.Inheritance r'''
class validation:
    def validate(self,age):
        if(age>18):
            return "Eligible"
        else:
            return "Not eligible"
class voterid:
    def fun1(self,age):
        p1=validation()
        self.retVal=p1.validate(age)
    def disp(self):
        print(f"Person is {self.retVal} for voting")
class drivingLicense:
    def fun1(self,age):
        p1.validation()
        self.retVal=p1.validate(age)
    def disp(self):
        print(f"Person is {self.retVal} for driving")
# v1=voterid()
# v1.fun1(30)
# v1.disp()
# d1=drivingLicense()
# d1.fun1(17)
# d1.disp()

class engine:
    def start(self):
        print("Engine Started")
    def stop(self):
        print("Engine Stopped")
class door:
    def open(self):
        print("Door opened")
    def close(self):
        print("Door closed")
class car:
    e1=engine()
    d1=door()

c1=car()
# c1.e1.start()
# c1.d1.open()
# c1.d1.close()

'''WAP in python of student entity and application should also allow user to deal with services for many students
it should read subject marks average, find min average score,should ask how many student data to be entered,read each student data and store it in array,do 
ask if user want to display minVal of avg score'''
class Student:
    l1=[]
    def __init__(self, name,scode,score):
        self.name = name
        self.scode = scode
        self.score = score

    def appending(self):
        self.l1.append(self.score)
    
    def Findmin(self):
        print(min(self.l1))
while(True):
    print("1.Student detail\n2.Finf min\n3.Exit")
    option=int(input("Enter the option"))
    if(option==1):
        name = input("Enter the name ")
        scode= input("Enter the score ")
        marks=int(input("Enter marks: "))
        s1=Student(name,scode,marks)
        s1.appending()
    elif(option==2):
        s1.Findmin()
    
    else:
        exit()









