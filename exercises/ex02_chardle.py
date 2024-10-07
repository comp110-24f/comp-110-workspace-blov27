"""Wordle clone- exercise 02"""

__author__: str = "730646728"
# identifies this file as being unique to me and my PID


# The input_word function took me like 10 minutes to make-
# the hardest part for me was figuring out how to store user input as a variable, but I eventually got it!


def input_word() -> str:
    """Takes input from a user, which should idealy be a 5 letter word"""
    custom_word: str = input("Enter a 5-character word: ")
    if len(custom_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return custom_word


# The input_letter function was very easy for me to make after making the input_word function: I just did the exact same thing except I checked to see if the length of the input string was 1.


def input_letter() -> str:
    """Takes input from a user, needs to be a single letter"""
    custom_letter: str = input("Enter a single character: ")
    if len(custom_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return custom_letter


# the contains_char function is the meat of this program and searches the input word for any instances of the input letter
# i definitely spent more time making this function than i spent making the other functions


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    letter_count: int = 0
    # these many if statements could have been made as a loop, but i wasn't sure if that was a forbidden construct
    if letter == word[0]:
        print(letter + " found at index 0")
        letter_count += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        letter_count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        letter_count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        letter_count += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        letter_count += 1
    if letter_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif letter_count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(letter_count) + " instances of " + letter + " found in " + word)


# the main function allows the program to run nicely in a single function!
def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# the following command allows for my program to run as soon as it is opened
if __name__ == "__main__":
    main()
