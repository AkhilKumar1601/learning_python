# files = ["1.txt","2.txt","3.txt"];

# for file in files:
#   try:
#     with open(file,"r") as f:
#       print(f.read());
#   except FileNotFoundError:
#     print(f"{file} is not present");

# l = [1,3,4,5,5,8,0,32,33];

# for i,item in enumerate(l):
#   if i == 2 or i == 4 or i == 6:
#     print(f"Value on {i+1} place is: {item}")


# n = int(input("Enter the number for which you want the table: "))
# l = [f"{n} x {i} = {n*i}\n" for i in range(1,11)];
# # print(l);

# a = int(input("Enter the value for a: "))
# b = int(input("Enter the value for b: "))

# try:
#     print(a / b)

# except ZeroDivisionError:
#     print("infinite")

# with open("tables.txt","w") as f:
#   f.writelines(l);
  

