"""Practice with conditional statements"""


def less_than_10(num: int) -> None:
    """Tells me if num is less than 10"""
    if num < 10:
        print("This number is less than 10")
    elif num == 10:
        print("This number is 10!")
    else:
        print("This number is greater than 10")


less_than_10(num=10)


def hungry(hunger: bool) -> None:
    """Helps me determine if I should get food or not"""
    if hunger == True:
        print("Go eat, you greedy pig")
    else:
        print("Don't eat, you're too fat")


hungry(True)


def check_first_letter(word: str, letter: str) -> str:
    """Checks to see if the first letter of a given word matches the inputted letter"""
    if word[0] == letter:
        return "Match!"
    else:
        return "No match :("


print(check_first_letter(word="Ford", letter="F"))
