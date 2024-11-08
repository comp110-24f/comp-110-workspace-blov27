"""Definitions for 3 different functions relating to lists"""


def get_first(l1: list[str]) -> str:
    """takes a list of strings and returns the first element"""

    return l1[0]


def remove_first(l2: list[str]) -> None:
    """modifies a list by removing its first element"""
    l2.pop(0)


def get_and_remove_first(l3: list[str]) -> str:
    """modifies a list by removing its first element and returns the deleted value"""
    first_val: str = l3[0]
    l3.pop(0)
    return first_val
