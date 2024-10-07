"""Mutating functions."""

__author__ = "730646728"


def manual_append(initial_list: list[int], num_to_add: int) -> None:
    """Appends an existing list by adding an additional number to it"""
    initial_list.append(num_to_add)


def double(input_list: list[int]) -> None:
    """Modifies an existing list by doubling every individual value"""
    index: int = 0
    while index < len(input_list):
        input_list[index] = 2 * input_list[index]
        index += 1


# a: list[int] = [1, 2, 3]
# manual_append(a, 2)
# print(a)
# double(a)
# print(a)


list1: list[int] = [1, 2, 3]
list2: list[int] = list1

double(list2)
print(list1)
print(list2)
