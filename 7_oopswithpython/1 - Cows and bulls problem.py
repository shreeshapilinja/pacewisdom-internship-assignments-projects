import random

def generate_secret_number():
    return ''.join(random.sample('0123456789', 4))

def count_cows_and_bulls(secret_number, guess):
    cows = sum(1 for s, g in zip(secret_number, guess) if s == g)
    bulls = sum(1 for g in guess if g in secret_number) - cows
    return cows, bulls

def main():
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to the Cows and Bulls Game!")
    print("Try to guess the 4-digit number with no repeated digits.")

    while True:
        guess = input("Enter your guess: ")
        
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input. Please enter a 4-digit number with no repeated digits.")
            continue
        
        attempts += 1
        cows, bulls = count_cows_and_bulls(secret_number, guess)
        
        if cows == 4:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        else:
            print(f"{cows} cows, {bulls} bulls")

if __name__ == "__main__":
    main()
