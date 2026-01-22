class Mobile:
    brand = "Redmi";
    price = 35000;

    def call(self):
        print("Mobile is calling");

    def message(self):
        print("Mobile is messaging");

m_1 = Mobile();
m_1.call();
m_1.message();

class Student:
    pass

class Employee:
    pass

harry = Employee();
s1 = Student();
print(s1);

class Book:
    name = "Rich Dad poor Dad";
    pages = 148;

    def book_details(self):
        print(f"The name of books is {self.name}.\nThis book consists of {self.pages}");

book_1 = Book();
book_1.book_details();

class Car:
    wheels = 4;

c1 = Car();
c2 = Car();

print(c1.wheels);
print(c2.wheels);

Car.wheels = 6;

print(c1.wheels);
print(c2.wheels);

class StaticEmployee:
    @staticmethod
    def greet():
        print("Hello user");

se = StaticEmployee();
se.greet();
