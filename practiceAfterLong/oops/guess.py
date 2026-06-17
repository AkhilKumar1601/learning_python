import random;

randNum = random.randint(1,100);
guess = 0;
guessedNumber = -1;
while (guessedNumber != randNum):
  guessedNumber = int(input("Guess the Number: "))
  if (guessedNumber > randNum):
    print("You have guessed higher number, guess lesser number: ");
  elif (guessedNumber < randNum):
    print("You have guessed lower number, guess higher number: ");
  guess += 1;

print(f"You have guessed the correct number in: {guess} guesses.")

if __name__ == "__main__":
 print("Running directly")

