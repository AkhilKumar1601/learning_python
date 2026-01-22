""" Task 1

class Animal:
    pass

class Dog(Animal):
    pass
"""

""" Task 2 - Single Inheritance

class Vehicle:
    def start(self):
        print("Starting the vehicle");

class Bike(Vehicle):
    def ride(self):
        print("You are riding bike");


b1 = Bike();
b1.start();
b1.ride();
"""
""" Task 3 - Multiple inheritance

class Employee:
    company = "Google";

class Freelancer:
    level = 1;

class Programmer(Employee,Freelancer):
    pass

p1 = Programmer();
print(p1.company);
print(p1.level);

class Camera:
    def take_photo(self):
        print("Taking photo");

class Phone:
    def call(self):
        print("Calling");

class SmartPhone(Camera,Phone):
    pass

sm = SmartPhone();
sm.take_photo();
sm.call();

# Multilevel inheritance

class LivingBeing:
    a = 1;

class Animal(LivingBeing):
    b = 2;

class Dog(Animal):
    c = 3;

d = Dog();
print(d.c,d.b,d.a);

#Super()  Method

class Employee:
    def __init__(self,name):
        self.name = name;

class Programmer(Employee):
    def __init__(self,name,language):
        super().__init__(name);
        self.language = language;

p = Programmer("Akhil","python");
e = Employee("Chetanya");

print(p.name);
print(p.language);
print(e.name);

"""
"""
# @classmethod

class Employee:
    company = "Google"

    @classmethod
    def changeCompany(cls, new_company):
        cls.company = new_company

Employee.changeCompany("Microsoft")
print(Employee.company);

class School:
    school_name = "ABC public school";

    @classmethod
    def changeSchool(cls, new_school):
        cls.school_name = new_school;

School.changeSchool("XYZ public school");
print(School.school_name);

"""
"""
# @property - getter, @name_of_property.setter

class Employee:
    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self,value):
        self.ename = value;

e = Employee();
e.ename = "Akhil";
print(e.name);
"""
"""
class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        return self.num + num2.num

n1 = Number(4);
n2 = Number(4);
print(n1+n2);

"""
"""
# Dunder method - __str__, __len__ for class.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}"

    def __len__(self):
        return len(self.marks)

s = Student("Akhil", [80, 85, 90])
print(s)        # calls __str__()
print(len(s))   # calls __len__()
"""
