import random

def play_hangman():
    words = ["python", "hangman", "internship", "keyboard", "programming"]
    word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print(f"You have {attempts_left} incorrect guesses allowed.\n")

    while attempts_left > 0:
        # Build the current display of the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)

        # Check for win
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

    if attempts_left == 0:
        print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()