
import os
import hangman


def test_get_word_no_punctuation():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_get_word_no_proper_nouns():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("Noufal\n")
        f.write("John\n")
        f.write("Simon\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_get_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_mask_word_a_letter():
    secret_word = "aligator"
    guesses = ["g"]
    ret = hangman.hangman_mask(secret_word, guesses)
    assert ret == "---g----"


def test_mask_word_multiple_letters():
    secret_word = "aligator"
    guesses = ["a"]
    ret = hangman.hangman_mask(secret_word, guesses)
    assert ret == "a---a---"


def test_mask_word_mixed_letters():
    secret_word = "aligator"
    guesses = ["a", "g", "w"]
    ret = hangman.hangman_mask(secret_word, guesses)
    assert ret == "a--ga---"


def test_create_status_no_guesses():
    secret_word = "aligator"
    guesses = []
    remaining_turn = 8
    ret = hangman.hangman_create_status(secret_word, guesses, remaining_turn)
    assert ret == """Word:--------
    Guesses:
    Remaining_turns:8"""


def test_create_status_normal():
    secret_word = "aligator"
    guesses = ["a", "g", "h"]
    remaining_turns = 4
    ret = hangman.hangman_create_status(secret_word, guesses, remaining_turns)
    assert ret == """Word:a--ga---
    Guesses:a g h
    Remaining_turns:4"""
