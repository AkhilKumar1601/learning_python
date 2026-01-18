a = 3;
b = 4.5;
c = "Akhil";
e = True;
f = None;

print("Variables:", a, b, c, e, f);

a += 1;
print(a);

print("Types of variables:", type(a), type(b), type(c), type(e), type(f));

g = str(a);
h = float(a);
i = int(b);

print(g, h, i);

print("Type check after converting type:", type(g), type(h), type(i));

input = input("Enter name: ");
print(input);

number1 = 33;
number2 = 4;

print("Addition of number1 and number2: ", number1+number2);
print("Remainder: ", number1%number2);
print("Type of input variable : ", type(input));

