import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
    print("🎲 I am thinking of a number between 1 and 99...")
    
    guess = None
    attempts = 0  
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")

    print(f"🎉 Congrats! The number was {secret_number}.")
    print(f"You guessed it in {attempts} attempt(s)!")

if __name__ == '__main__':
    main()
