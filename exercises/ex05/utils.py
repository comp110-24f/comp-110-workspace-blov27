"""Practice creating utility functions: exercise 05"""

__author__: str = "730646728"


def only_evens(input_list: list[int]) -> list[int]:
    """creates a new list that contains the even values from a previous list"""
    # empty list that will have values added to it
    return_list: list[int] = []
    # loops through input list and records even values
    for vals in input_list:
        if vals % 2 == 0:
            return_list.append(vals)
    return return_list


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """returns a new list that is a subset of a previous list in a specified range"""
    return_list: list[int] = []
    # compensates for possibility that start index is negative
    if start_index < 0:
        start_index = 0
    # compensates for the possibility that the end index is out of the list's bounds
    if end_index > len(input_list):
        end_index = len(input_list)
    # collects values in the specified bounds and logs them in a new list
    for vals in range(start_index, end_index):
        return_list.append(input_list[vals])
    return return_list


def add_at_index(input_list: list[int], additional_value: int, user_index: int) -> None:
    """modifies an existing list by adding
    a new value to the list at a specified index"""
    if user_index < 0 or user_index > len(input_list):
        raise IndexError("Index is out of bounds for the input list")
    # raises an error message if user's Index input doesn't make since

    list_end: list[int] = []
    # collects a list of values greater than the target index
    for vals in range(user_index, len(input_list)):
        list_end.append(input_list[vals])

    dev_index: int = user_index

    while dev_index < len(input_list):
        input_list.pop(dev_index)
    # removes all values in the list that are futher than the target value

    input_list.append(additional_value)
    for vals in list_end:
        input_list.append(vals)
    # adds values after the target value to the end of the list
