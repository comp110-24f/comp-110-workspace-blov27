"""testing function defined in find_max"""

__author__ = "730646728"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_expected_val() -> None:
    """ensures that running find_and_remove_max returns the greatest value in the list"""
    c: list[int] = [9, 9, 6, 7]
    assert find_and_remove_max(c) == 9
    # test should return True


def test_find_and_remove_max_mutates_correctly() -> None:
    """ensures that the return list is correctly modified"""
    b: list[int] = [10, 9, 8, 5, 10]
    find_and_remove_max(b)
    assert b == [9, 8, 5]
    # test should return True


def test_find_and_remove_max_edge_case() -> None:
    """ensures that the edge case of an empty list returns -1"""
    a: list[int] = []
    assert find_and_remove_max(a) == -1
    # test should return True
