"""Reverse engineering algorithms: exercise 04"""

__author__: str = "730646728"


# checks to see if all values in a list are equal to an imported number
def all(collection: list[int], num: int) -> bool:
    if len(collection) == 0:
        return False
    for values in collection:
        if values != num:
            return False
    return True


# outputs the greatest integer in a given list
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    greatest: int = input[0]
    for values in input:
        if values > greatest:
            greatest = values
    return greatest


# checks to see if two lists are identical to each other
def is_equal(l1: list[int], l2: list[int]) -> bool:
    # makes sure that lists are the same length
    # returns False if the lists are different lengths
    if len(l1) != len(l2):
        return False
    # runs through each character of a word
    index: int = 0
    while index < len(l1):
        if l1[index] != l2[index]:
            return False
        else:
            index += 1
    return True


# combines two lists together by looping through the built in 'append' function
def extend(list1: list[int], list2: list[int]) -> None:
    for elements in list2:
        list1.append(elements)


a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]
