"""Third challenge question assignment- Practice with while loops"""

__author__ = "730646728"


# this is my function that i made in COMP110 class!
def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    tally: int = 0
    # the count variable records how many characters have been compared to the search character
    # the tally variable records how many instances of the search character are present in the function
    while count < len(phrase):
        if search_char == phrase[count]:
            tally = tally + 1
            count = count + 1
        else:
            count = count + 1

    # this loop runs until every charater has been checked for its similarity to the search character
    return tally
    print(tally)
