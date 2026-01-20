import math;

class Calculator:

    def __init__(self,user_name):
        self.user_name = user_name;

    def get_square(self,num):
        return num * num;

    def get_cube(self,num):
        return num * num * num;

    def get_square_root(self,num):
        return math.sqrt(num);


user_1 = Calculator("Akhil");
print(user_1.get_square(4));
print(user_1.get_cube(4));
print(user_1.get_square_root(64));

