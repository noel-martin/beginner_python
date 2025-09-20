import random
def number_guessing_game():
  number = random.randint(1, 100)
  attempts=0
  print("Welcome to the Number guessing game.")
  print("I'am thinking of a number between 1 and 100.")
  while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {number}.")
            print(f"You guessed it in {attempts} tries.")
            break

number_guessing_game()