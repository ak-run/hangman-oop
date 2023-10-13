import random
import csv


class WordToGuess:
    def __init__(self):
        """
        Initialize the WordToGuess class with an empty word_list attribute.
        """
        self.word_list = []

    def random_word_from_csv_file(self, csv_filename: str):
        """
        Select a random word from a CSV file and return it.
        """
        # Open and read the CSV file
        with open(csv_filename, 'r') as file:
            reader = csv.reader(file)
            # Use list comprehension to extract words from rows
            self.word_list = [row[0] for row in reader]
        # Select a random word from the list
        return random.choice(self.word_list)

    def words(self):
        """
        Return the word_list attribute containing words from the CSV file.
        """
        return self.word_list
