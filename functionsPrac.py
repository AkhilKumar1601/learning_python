#create a function to check which no. is greater.

def check_max(no_1,no_2,no_3):
    if ( no_1 > no_2 and no_1 > no_3 ):
        print("First that you have entered is greatest");
    elif (no_2 > no_3 and no_2 > no_1):
        print("Second that you have entered is greatest");
    else:
       print("Third that you have entered is greatest");

check_max(10,8,9);

#function to convert celsius to fahrenheit.
def convert_temperature(cel_temp):
    return (cel_temp * (9/5)) + 32;

print(convert_temperature(25));

#Write a recursive function to calculate the sum.
def get_sum(n):
    if (n==1):
        return 1;
    return n + get_sum(n-1);

print(get_sum(5));


# function to print pattern
def print_pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ");
        print("\n");

print_pattern(3);
