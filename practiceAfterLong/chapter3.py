from datetime import datetime

name = input("Enter your Name: ")
print("Good Afternoon, ",name)

letter = '''
Dear <|Name|>
You are selected!
Date: <|Date|>
Current Time: <|Time|>
'''

now = datetime.now();
date = now.date();
time = now.time();

letter = letter.replace("<|Name|>",str(name))
letter = letter.replace("<|Date|>",str(date))
letter = letter.replace("<|Time|>",str(time))

print(letter)

stringVariable = "hello  ji  kaisa ho   ji";
print(stringVariable.find("  "))

updatedStringVariable = stringVariable.replace("  "," ")
print(updatedStringVariable)

letter2 = "Dear Harry,\n\tThis Python course is nice.\nThanks!"
print(letter2)
