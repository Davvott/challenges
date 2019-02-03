#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    draw = []
    for num in range(NUM_LETTERS):
        rand_choice = POUCH.pop(random.choice(range(len(POUCH))))
        draw.append(rand_choice)
    return draw


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    # Get word
    user_input = input('Enter a word from your tiles: ').upper()
    # If not valid, keep trying
    while _validation(user_input, draw) is False:
        print('Word cannot be played, try again.')
        user_input = input('Enter a word from your tiles: ').upper()
    return user_input.title()


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    # Valid Word
    draw_copy = draw[:]

    if word not in DICTIONARY:
        print('Word not in Dictionary')
        return False
    else:  # Valid word from draw
        for char in word:
            if char not in draw_copy:
                return False
            else:
                draw_copy.pop(draw_copy.index(char))
        return True


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    poss_words = _get_permutations_draw(draw)
    return [word for word in poss_words if word in DICTIONARY]


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    perm_words = []

    for i in range(1, len(draw)):
        for word in itertools.permutations(draw, i):
            if ''.join(word) in DICTIONARY:
                perm_words.append(''.join(word))
    return perm_words


# From challenge 01:
def max_word_value(words=DICTIONARY):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
