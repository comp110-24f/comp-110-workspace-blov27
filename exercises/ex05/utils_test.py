"""testing function defined in utils"""

__author__ = "730646728"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return() -> None:
    """Checks to make sure only evens returns even values"""
    list1: list[int] = [1, 2, 3, 5, 7, 9]
    assert only_evens(list1) == [2]


def test_only_evens_no_mutate() -> None:
    """Checks to make sure that the input list is not mutated by only_evens"""
    list1: list[int] = [1, 2, 3, 5, 7, 9]
    only_evens(list1)
    assert list1 == [1, 2, 3, 5, 7, 9]


def test_only_evens_edge_case() -> None:
    """Tests an edge case for only_evens"""
    # only_evens on an empty list should return an empty list
    assert only_evens([]) == []


def test_sub_functionality() -> None:
    """Validates that running sub on a function returns the correct segement of the input list"""
    list1: list[int] = [4, 5, 6, 7, 8]
    assert sub(list1, 2, 5) == [6, 7, 8]


def test_sub_no_mutate() -> None:
    """Asserts that utilizing sub does not modify the input list"""
    list1: list[int] = [11, 12, 13]
    sub(list1, 0, 1)
    assert list1 == [11, 12, 13]


def test_sub_edge_case() -> None:
    """Checks an edge case for sub"""
    empty_list: list[int] = []
    assert sub(empty_list, 1, 7) == []


def test_add_at_index_return() -> None:
    """Checks to make sure add_at_index returns the expected list"""
    list1: list[int] = [2, 3, 4, 5, 7]
    add_at_index(list1, 6, 4)
    assert list1 == [2, 3, 4, 5, 6, 7]


def test_add_at_index_mutate() -> None:
    """Checks to make sure add_at_index modifies the input list"""
    list1: list[int] = [1, 2, 4]
    add_at_index(list1, 3, 2)
    assert list1 != [1, 2, 4]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    a = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(a, 3, 8)
        # an IndexError is raised for the case when the add_at_index is
        # given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
