import random


def get_word(wordfile="/usr/share/dict/words"):
    good_words = []
    with open(wordfile) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) >= 5:
                good_words.append(i)
    return random.choice(good_words)


def hangman_mask(secret_words, guesses):
    result_string = []
    for i in secret_words:
        if i in guesses:
            result_string.append(i)
        else:
            result_string.append("-")
    return "".join(result_string)


def hangman_create_status(secret_words, guesses, remaining_turn):
    masked_word = hangman_mask(secret_words, guesses)
    guessed = " ".join(guesses)
    return f"""Word:{masked_word}
    Guesses:{guessed}
    Remaining_turns:{remaining_turn}"""


def hangman_play(secret_words, guesses, remaining_turn, guessed):
    if "-" not in hangman_mask(secret_words, guesses+[guessed]):
        return remaining_turn, False, True
    if guessed in guesses:
        return remaining_turn, True, False
    if guessed in secret_words:
        guesses.append(guessed)
        return remaining_turn, False, False
    if guessed not in secret_words:
        guesses.append(guessed)
        return remaining_turn-1, False, False


def main():
    secret_word = get_word()
    print(secret_word)
    remaining_turns = 8
    guesses = []
    while True:
        status = hangman_create_status(secret_word, guesses, remaining_turns)
        print(status)
        guessed = input("Enter a letter ").strip()
        remaining_turns, repeat, finished = hangman_play(
            secret_word, guesses, remaining_turns, guessed)
        if finished:
            print(f"You found the secret word '{secret_word}'")
            break
        if remaining_turns == 0:
            print(f"You failed. The secret word was {secret_word}")
            break
        elif repeat:
            print(f"You already guessed '{guessed}'")


if __name__ == "__main__":
    main()
