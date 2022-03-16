
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


def test_correct_guess():
    secret_word = "aligator"
    guesses = []
    remaining_turns = 5
    guessed = "a"
    remaining_turns, repeat, finished = hangman.hangman_play(
        secret_word, guesses, remaining_turns, guessed)
    assert guesses == ["a"]
    assert remaining_turns == 5
    assert repeat == False
    assert finished == False


def test_play_correct_wrong():
    secret_word = "aligator"
    guesses = ["a"]
    remaining_turns = 7
    guessed = "x"
    remaining_turns, repeat, finished = hangman.hangman_play(
        secret_word, guesses, remaining_turns, guessed)
    assert guesses == ["a", "x"]
    assert remaining_turns == 6
    assert repeat == False
    assert finished == False


def test_play_correct_complete():
    secret_word = "aligator"
    guesses = ["a", "e", "w", "t", "l", "i", "o", "g", "r", "u", "w"]
    remaining_turns = 2
    guessed = "r"
    remaining_turns, repeat, finished = hangman.hangman_play(
        secret_word, guesses, remaining_turns, guessed)
    assert finished == True


def test_play_round_correct_repeat():
    secret_word = "aligator"
    guesses = ["a"]
    remaining_turns = 4
    guessed = "a"
    remaining_turns, repeat, finished = hangman.hangman_play(
        secret_word, guesses, remaining_turns, guessed)
    assert guesses == ["a"]
    assert remaining_turns == 4
    assert repeat == True
    assert finished == False
