score = int(input("Enter your previous score: "));

try:
   f = open("hi_score.txt","r");
   data = f.read();
   f.close();

   if data == "":
        high_score = 0;
   else:
        high_score = int(data);

except FileNotFoundError:
    high_score = 0;


if high_score < score:
    f = open("hi_score.txt","w");
    f.write(str(score));
    f.close();
    print("New score updated");
else:
    print("Good try! Hi score is still same: ",high_score);
