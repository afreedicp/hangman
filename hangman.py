import random


def get_word(wordfile="/usr/share/dict/words"):
    good_words = []
    with open(wordfile) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) >= 5:
                good_words.append(i)
    return random.choice(good_words)


def hangman_mask(secrete_words, guesses):
    result_string = []
    for i in secrete_words:
        if i in guesses:
            result_string.append(i)
        else:
            result_string.append("-")
    return "".join(result_string)
