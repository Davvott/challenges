#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    pass
    # draw = draw_letters()
    # Display drawn Letters
    # Get user_input() for possible word
    # Validate user_input, else continue asking
    # Compare user_input against all permutations of drawn letters
    # Obvs only valid permutations to be passed back
    # Display highest scoring possible word -> max_word_value(permutations)


if __name__ == "__main__":
    main()
