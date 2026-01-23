import random

def guessNumber():
    num = random.randint(1,100);
    no_of_guess = 0;

    while True:
        guessed_number = int(input("Enter the number: "));
        no_of_guess += 1;
        if(guessed_number > num):
            print("You have guessed greater number, please choose smaller number than this");
        elif(guessed_number < num):
            print("You have guessed smaller number, please choose greater number than this");
        else:
            print(f"Congratulations! you have guessed the right number in {no_of_guess} guesses.");
            break;


guessNumber();
