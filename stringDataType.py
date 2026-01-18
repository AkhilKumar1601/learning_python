from datetime import date, timedelta;

print("Hello ji \nI am Akhil Kumar.");
name = input("Enter your name: ");
print(name ,"\nGood After sir");

current_date = date.today();
selection_date = current_date + timedelta(days=2);

print(f'''
        Dear {name},
        You are selected!
        {selection_date}>
        ''');

txt = "Hello  ji Kaisa ho ji";
if "  " in txt:
    print("Double space found");
else:
    print("No double space found");

double_space_count = txt.count("  ");
print("No. of double space in txt: ",double_space_count);

clean_txt = " ".join(txt.split());
print(clean_txt);

letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)

