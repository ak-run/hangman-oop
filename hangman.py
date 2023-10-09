class Hangman:
    def __init__(self):
        """
        Initialize Hangman game with a list of hangman_pictures and lives.
        """
        self.hangman_pictures = []
        self.lives = 0

    def set_difficulty(self, difficulty):
        """
        Set the game difficulty level and initialize hangman_pictures and lives accordingly.
        """
        if difficulty == "easy":
            self.hangman_pictures = ["       \n       \n      |\n      |\n      |\n      |\n=========",
                                     "       \n      |\n      |\n      |\n      |\n      |\n=========",
                                     "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="][::-1]  # Reverse the order
            self.lives = 10
        elif difficulty == "medium":
            self.hangman_pictures = ["  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="][::-1]  # Reverse the order
            self.lives = 8
        elif difficulty == "hard":
            self.hangman_pictures = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
                                     "  +---+\n  |   |\n  O   |\n /|\\  |\n / \  |\n      |\n========="][::-1]  # Reverse the order
            self.lives = 6

    def display_hangman(self):
        """
        Display the Hangman figure corresponding to the current number of lives.
        """
        if self.lives < len(self.hangman_pictures):
            print(self.hangman_pictures[self.lives])
        else:
            print("Game over! You lost.")