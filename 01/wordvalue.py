from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        all_words = [''.join(line.strip().split('-')) for line in f]
    return all_words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    word = word.upper()
    for letter in word:
        value += LETTER_SCORES[letter]
    return value


def max_word_value(word_list=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    curr_max = 0
    max_word = ''
    for word in word_list:
        val = calc_word_value(word)
        if val > curr_max:
            curr_max = val
            max_word = word
    return max_word


if __name__ == "__main__":
    pass    # run unittests to validate
