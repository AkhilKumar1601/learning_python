# Find an multiplication of an number.

n = int(input("Enter your number"));

for i in range(10):
    print((i+1) * n);

#Greet by their name.
l = ["Harry","Sachin","Soham","Rahul"]

for name in l:
    print(f"\n Hello {name} \n \t Good Afternoon sir.");


#Attempt problem 1 using while loop.
i = 1;

while (i<=10):
    print(i*n);
    i += 1;

#Check wheather a number is prime or not.
ni = int(input("Enter your number"));

itr = 2;
while (itr < ni):
    if (ni % itr == 0):
        print("This is not a prime number");
        break;
    itr += 1;
else:
    print("This is a prime number");

#sum of first n natural numbers
sn = int(input("Enter your number: "));
sum = 0;
iter = 1;
while (iter <= sn):
    sum += iter;
    iter += 1;

print(sum);

#find factorial of a number;
fn = int(input("Enter your number: "));
fact = 1;
itr2 = 2;
while (itr2 <= fn):
    fact *= itr2;
    itr2 += 1;

print(fact);
