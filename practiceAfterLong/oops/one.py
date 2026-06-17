import math,random;
# class Programmer:
#   company = "Microsoft";

#   def __init__(self,name,date_of_joining,department):
#     self.name = name;
#     self.date_of_joining = date_of_joining;
#     self.department = department;

# p1 = Programmer("Akhil", "17-06-2026", "Engineering")
# p2 = Programmer("Rahul", "01-01-2026", "HR")

# print(p1.name)
# print(p1.company)
# print(p2.department)

# class Calculator:

#   @staticmethod
#   def greetUser():
#     print("Hello, welcome in calculator");

#   def __init__(self,number):
#     self.number = number;

#   def getSquare(self):
#     return self.number * self.number;
  
#   def getCube(self):
#     return self.number * self.number * self.number;

#   def getSquareRoot(self,number):
#     return math.sqrt(self.number);

# Calculator.greetUser();

# c = Calculator(4);
# squareNumber = c.getSquare();
# print(c.getSquareRoot(squareNumber))

# class Check:
#   a = 12;

# ch1 = Check();
# ch1.a = 0;
# print(ch1.a);
# print(Check.a);

class Train:

  def book_ticket(self):
    print("Your ticket is booked");

  def get_status(self):
    return random.randint(1,100);

  def get_fare(self):
    return 750;

passenger1 = Train();
passenger1.book_ticket();
print(passenger1.get_status());
print(passenger1.get_fare());