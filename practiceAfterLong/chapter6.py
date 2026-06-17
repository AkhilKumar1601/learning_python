# age = int(input("Enter your age: "));

# if (age >= 18):
#   print("You are eligible for voting")
# else:
#   print("You are not eligible for voting")

# greatest_number = -1;
# for i in range(0,4):
#   number = int(input("Enter your Number: "));
#   if (number > greatest_number):
#     greatest_number = number;

# print("The greatest out of 4 you have entered is: ",greatest_number);

# percentage_per_subject = [];
# total_percentage = 0;
# for i in range(1,4):
#   percentage = int(input("Enter your percentage in subject {i}: "));
#   total_percentage += percentage;
#   percentage_per_subject.append(percentage);

# average_percentage = total_percentage/3;

# if ( average_percentage >= 40 and min(percentage_per_subject) >= 33 ):
#   print("You are pass");
# else:
#   print("You are fail");



spam_list = ["make a lot of money", "buy now", "subscribe this", "click this"]

comment = input("Type your comment: ").lower()

is_spam = False

for junk in spam_list:
    if junk in comment:
        is_spam = True
        break

if is_spam:
    print("This comment is spam")
else:
    print("This comment is not spam")




