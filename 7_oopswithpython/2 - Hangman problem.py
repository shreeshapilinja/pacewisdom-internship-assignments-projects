import random
def read_words_from_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().splitlines()
    return words

def choose_random_word(word_list):
    return random.choice(word_list)

def init_game():
    word_list = read_words_from_file('words.txt')
    chosen_word = choose_random_word(word_list)
    guessed_letters = []
    return chosen_word, guessed_letters

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def play_game():
    print("Welcome to Hangman!")

    while True:
        chosen_word, guessed_letters = init_game()
        remaining_attempts = 6
        print(display_word(chosen_word, guessed_letters))
        while remaining_attempts > 0:
            guess = input("Guess your letter: ").upper()
            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue
            guessed_letters.append(guess)            
            if guess in chosen_word:
                print(display_word(chosen_word, guessed_letters))
            else:
                remaining_attempts -= 1
                print("Incorrect!")
                print(f"You have {remaining_attempts} {'chance' if remaining_attempts == 1 else 'chances'} left.")

            if "_" not in display_word(chosen_word, guessed_letters):
                print("Congratulations! You guessed the word:", chosen_word)
                break
        if remaining_attempts == 0:
            print("Sorry, you've run out of chances. The word was:", chosen_word)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    play_game()
