"""defining a function that finds the max value in a string and removes it"""

__author__ = "730646728"


def find_and_remove_max(input_list: list[int]) -> int:

    if input_list == []:
        return -1  # edge case where user imputs an empty string
    else:
        max_val: int = input_list[
            0
        ]  # logs the current max value, is the first value by default
        index: int = 0

        for vals in input_list:
            # for loop cycles through each element in the list and checks to see if it is larger than the current max value
            if max_val < vals:
                max_val = vals

        while index < len(input_list):
            # this while loop finds every instance of the max value in the input list and modifies the list by removing these values
            if input_list[index] == max_val:
                input_list.pop(index)
                index = 0  # deleting a value from the list offsets the positions of the other values, so i am resetting the index to make sure we don't skip any values
            else:
                index += 1

        return max_val  # returns largest element in the list
