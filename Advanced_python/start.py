"""
n = [1,2,2,3];
if len(n) > 3:
    print(n);
"""
"""
#walrus operator (Assignment + condition)
if (len(n := [1,2,3,4])) > 3:
    print(n);

if len(n := input("Enter something: ")) > 5:
    print(n);
"""
"""

#Type defination
num : int = 8;
def print_str(name: str):
    print(f"Hello, {name}");

print_str("Akhil");
print(num);

def square(n : int) -> int:
    return n * n;

print(square(8));

"""
"""
#Advanced type hints
from typing import List, Tuple, Dict, Union

numbers : List[int] = [1,2,3];
person : Tuple[str,int] = ("Akhil",22);
marks : Dict[str,int] = {"Math":90};
value : Union[str,int] = 10;

print(numbers, person, marks, value);

"""

"""
from typing import List, Dict

names : List[str] = ["Akhil","Chetanya","Pajii","Hardik","Naman"];
subjects_to_marks : Dict[str,int] = {
        "Maths" : 73,
        "Science" : 60,
        "English" : 65,
        "SST(Social studies)" : 68
        };

print(names, subjects_to_marks);

"""
"""
def check_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown"

print(check_status(300));

"""
"""
def get_first_two_days(n : int) -> str:
    match n:
        case 1:
            return "Sunday";
        case 2:
            return "Monday";
        case _:
            return "Invalid";

print(get_first_two_days(3));
"""
"""
d1 = {'a': 1}
d2 = {'b': 2}
d1 |= d2;
print(d1);
print(d2);
print(d1 | d2)
"""
"""
from typing import Dict

dict_1 : Dict[str,int] = {"Akhil" : 688};
dict_2 : Dict[str,int] = {"Chetanya" : 720};
dict_1 |= dict_2;
print(dict_1);

"""

"""
with (
    open("a.txt", "a+") as f1,
    open("b.txt", "a+") as f2
):
    f1.write("\nWhat is your Name?")
    f1.seek(0)
    print(f1.read())

    f2.write("\nMy name is Akhil")
    f2.seek(0)
    print(f2.read())
"""


