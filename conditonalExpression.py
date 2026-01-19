#Check if user is eligible for vote or not.

user_age = int(input("Enter your age: "));

if (user_age >= 18):
    print("User is eligible to vote");
else:
    print("User is not eligible to vote");

#Give me greatest number entered by user;
maxi = 0;

for i in range(4):
    n = int(input("Enter your number: "));
    if (n >= maxi):
        maxi = n;


print(maxi);

#Check student is passed or failed :- pass criteria total 40% and 33% in each subject;
percentage_list = []

print("We need your marks subject wise")
no_of_subjects = int(input("How many subjects you have: "))

for i in range(no_of_subjects):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    percentage = (marks / 80) * 100
    percentage_list.append(percentage)
    print("Percentage of this subject:", percentage);

total_percentage = sum(percentage_list) / len(percentage_list)

print("\nTotal Percentage:", round(total_percentage, 2))

if min(percentage_list) >= 33 and total_percentage >= 40:
    print("Congratulations! You are PASS 🎉")
else:
    print("You are FAIL")

#Check comment is spam or not.

comment = input("Enter your comment: ").lower();

spam_keywords = [
        "make a lot of money",
        "buy now",
        "subscribe this",
        "click this"
];

is_spam = False;

for words in spam_keywords:
    if words in comment:
        is_spam = True;
        print("Spam detected");
        break;

if (not is_spam):
   print("This is not a spam");

#Check username consist of more than 10 character or not.
username = input("Enter your username: ");
if (len(username) >= 10):
    print("Username consists of more than 10 characters");


#Check name is present in list or not.
names = ["Akhil", "Chetanya", "Pajii", "Rahul", "Aman"]

name = input("Enter the name to search: ")

if name in names:
    print("Name is present in the list ✅")
else:
    print("Name is not present in the list ❌")


