def func1():
  print("Hello");

func1();

def greetByName(name):
  print(f"Hello {name},\n\t Good Afternoon!")

greetByName("Akhil");

#Recursion
def factorial(n):
  if (n == 0 or n == 1):
    return 1;
  else:
    return n*factorial(n-1);

print(factorial(8));