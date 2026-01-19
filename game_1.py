import random;

def play_game():
    choices = ["snake","water","gun"];

    computer_choice = random.choice(choices);
    user = input("Enter either snake, water or gun: ").lower();

    print("Computer chooses: ",computer_choice);


    if user == computer_choice:
        print("Draw");
    elif (user=="snake" and computer_choice=="water") or (user=="water" and computer_choice=="gun") or (user=="gun" and computer_choice=="snake"):
        print("User win's");
    else:
        print("Computer wins's");

play_game();
