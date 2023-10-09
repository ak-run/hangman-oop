from hangman import Hangman
from word_to_guess import WordToGuess

def hangman_game():
    """
    Play a game of Hangman.
    """
    word_to_guess_obj = WordToGuess()  # Create an instance of WordToGuess
    word_to_guess = word_to_guess_obj.random_word_from_csv_file(csv_file)  # Get the random word
    word_string = "_" * len(word_to_guess)  # Initialize the word display with underscores
    guesses = []  # Store guessed letters
    print(word_string)

    # Continue the game until the word is guessed or the player runs out of lives
    while word_string != word_to_guess and hangman.lives > 0:
        guess = input("Guess a letter: ")

        if len(guess) == 1:
            # Check if the guessed letter is in the word_to_guess
            if guess in word_to_guess and guess not in guesses:
                # Replace underscores in word_string with correctly guessed letters
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        word_string = word_string[:i] + guess + word_string[i + 1:]
                print("Correct guess! Word:", word_string)
                guesses.append(guess)
            elif guess in guesses:
                print(f"You already tried {guess}, try another letter")
            else:
                hangman.lives -= 1
                print("Incorrect guess. Lives left:", hangman.lives)
                guesses.append(guess)
                hangman.display_hangman()  # Display Hangman picture
        else:
            if guess == word_to_guess:
                word_string = guess
                break
            else:
                hangman.lives -= 1
                print("Incorrect guess. Lives left:", hangman.lives)
                hangman.display_hangman()  # Display Hangman picture

    # Check if the player won or lost
    if word_string == word_to_guess:
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("Sorry, you ran out of lives. The word was:", word_to_guess)


if __name__ == "__main__":
    csv_file = "words.csv"
    difficulty = input("Choose difficulty easy/medium/hard: ")
    hangman = Hangman()
    hangman.set_difficulty(difficulty)
    hangman_game()