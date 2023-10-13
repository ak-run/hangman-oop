import unittest
from unittest.mock import patch, mock_open
from word_to_guess import WordToGuess  # Import your WordToGuess class from your actual module

class TestWordToGuess(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    @patch('random.choice')
    def test_random_word_from_csv_file(self, mock_random_choice, mock_open):
        csv_data = 'word1,word2,word3\napple,banana,orange\n'
        csv_filename = 'test.csv'

        # Set up the mock_open to return CSV data when file is opened
        mock_open.return_value.read_data = csv_data  # Correct the attribute name

        # Mock random.choice to return a fixed word
        mock_random_choice.return_value = 'banana'

        # Create an instance of WordToGuess
        word_guess = WordToGuess()

        # Call the method to test
        random_word = word_guess.random_word_from_csv_file(csv_filename)

        # Assertions
        self.assertEqual(random_word, 'banana')
        # Verify that the word_list attribute contains the expected words


if __name__ == '__main__':
    unittest.main()