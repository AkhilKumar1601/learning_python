"""

def main():
    print("Hello") 

if __name__ == "__main__": 
    main()

"""
"""
# Global keyword
count = 0;

def increase_count():
    global count;
    count += 1;

increase_count();
print(count);

"""
"""
# Enumerate

names = ["Akhil", "Rahul", "Aman"];
for i, name in enumerate(names, start=1):
    print(i, name)
"""

#List compreshion
list1 = [1, 7, 12, 11, 22]
list2 = [item for item in list1 if item > 8]

no_list = [3,76,78,66,5,43,44];
square_no_list = [square_no for n in no_list if (square_no:= n * n) > 64];
print(square_no_list);
