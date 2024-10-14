"""Summing the elements of a list using different loops"""

__author__ = "730646728"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    tally: float = 0
    while index < len(vals):
        tally += vals[index]
        index += 1
    return tally


def f_sum(vals: list[float]) -> float:
    tally: float = 0
    for num in vals:
        tally += num
    return tally


def f_range_sum(vals: list[float]) -> float:
    tally: float = 0
    for num in range(0, len(vals)):
        tally += vals[num]
    return tally


a: list[float] = [1.0, 2.0, 3.0, 5.5]
print(f_range_sum(a))
print(f_sum(a))
print(w_sum(a))
