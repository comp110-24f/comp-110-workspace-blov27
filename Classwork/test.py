"""Wordle game- exercise 03"""

__author__: str = "730646728"
# identifies this file as being unique to me and contains my PID


def input_guess(secret_word_len: int) -> str:
    """User choses number of characters to input, and then prompts user to enter that number of characters"""
    custom_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(custom_word) != secret_word_len:
        custom_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    # prints word that user inputted if it matches the established length
    return custom_word


def contains_char(input_word: str, test_char: str) -> bool:
    """Tests to see if a specific character is found within a specific word"""
    assert len(test_char) == 1
    # index variable is used to make sure we have checked every character of a word
    index: int = 0
    # instances records number of time that the search character has been found in the given word
    instances: int = 0
    # this loop makes sure we check the entire word
    while index < len(input_word):
        if test_char == input_word[index]:
            index += 1
            instances += 1
        else:
            index += 1
    # this operator returns a T/F value relating to if there are any instances of the search letter or not
    if instances == 0:
        return False
    else:
        return True


# function that determines what colors the emoji boxes should be
def emojified(user_word: str, hidden_word: str) -> str:
    """Compares a users guess to the hidden word and outputs emoji boxes"""
    assert len(user_word) == len(hidden_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    ans: str = ""
    while index < len(hidden_word):
        if user_word[index] == hidden_word[index]:
            index += 1
            ans += GREEN_BOX
        elif contains_char(user_word, hidden_word[index]):
            index += 1
            ans += YELLOW_BOX
        else:
            index += 1
            ans += WHITE_BOX
    return ans


# main function
def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    secret_word_len: int = len(secret)
    custom_word: str = input(f"Enter a {secret_word_len} character word: ")
    index: int = 1

    while index <= 6:
        while len(custom_word) != secret_word_len:
            custom_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
        print(f"=== Turn {index}/6 ===")
        print(emojified(custom_word, secret))
        # win message
        if custom_word == secret:
            print(f"You won in {index}/6 turns!")
            exit()
        # adds one to the index
        else:
            index += 1
            custom_word = input(f"Enter a {secret_word_len} character word: ")
    # fail message
    print(" X/6 - Sorry, try again tomorrow!")


# the following command allows for my program to run as soon as it is opened
if __name__ == "__main__":
    main(secret="codes")
