# class Vector2D:
#   def __init__(self,x,y):
#     self.x = x;
#     self.y = y;

# class Vector3D(Vector2D):
#   def __init__(self,x,y,z):
#     super().__init__(x,y);
#     self.z = z;

# v = Vector3D(1,2,3);
# print(v.x);
# print(v.y);
# print(v.z);

# class Animals():
#   pass

# class Pets(Animals):
#   pass


# class Dog(Pets):
#   @staticmethod
#   def bark():
#     print("Dog is barking");

# d = Dog();
# d.bark();

# class Employee:

#     def __init__(self, salary, increment):
#         self.salary = salary
#         self.increment = increment

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary * (1 + self.increment / 100)

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment = ((salary / self.salary) - 1) * 100


# e = Employee(50000, 10)

# print("Salary:", e.salary)
# print("Increment:", e.increment)
# print("Salary After Increment:", e.salaryAfterIncrement)

# e.salaryAfterIncrement = 60000

# print("\nAfter Updating Salary After Increment")
# print("Salary:", e.salary)
# print("Increment:", e.increment)
# print("Salary After Increment:", e.salaryAfterIncrement)

# class Complex:

#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def __add__(self, other):
#         return Complex(
#             self.real + other.real,
#             self.imaginary + other.imaginary
#         )

#     def __mul__(self, other):
#         return Complex(
#             self.real * other.real - self.imaginary * other.imaginary,
#             self.real * other.imaginary + self.imaginary * other.real
#         )

#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"


# c1 = Complex(2, 3)
# c2 = Complex(4, 5)

# print(c1 + c2)
# print(c1 * c2)

# class Vector:

#     def __init__(self, values):
#         self.values = values

#     def __add__(self, other):
#         result = []

#         for i in range(len(self.values)):
#             result.append(self.values[i] + other.values[i])

#         return Vector(result)

#     def __mul__(self, other):
#         dot_product = 0

#         for i in range(len(self.values)):
#             dot_product += self.values[i] * other.values[i]

#         return dot_product

#     def __str__(self):
#         return str(self.values)


# v1 = Vector([1, 2, 3])
# v2 = Vector([4, 5, 6])

# print(v1 + v2)
# print(v1 * v2)

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


v = Vector(7, 8, 10)

print(v)    