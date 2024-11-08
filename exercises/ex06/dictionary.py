"""practice with dictionaries"""

__author__ = "730646728"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Swaps the keys and values for a dictionary"""
    new_dict = dict()
    dict_check: dict[str, int] = dict()
    for keys in dictionary:
        new_dict[dictionary[f"{keys}"]] = keys
        if dictionary[f"{keys}"] in dict_check:
            dict_check[f"{dictionary[keys]}"] += 1
        else:
            dict_check[f"{dictionary[keys]}"] = 1
    for key3 in dict_check:
        if dict_check[f"{key3}"] > 1:
            raise KeyError("at least one key is entered more than once.")
    
    return new_dict


def favorite_color(responses: dict[str, str]) -> str:
    """Returns most popular color from a dictionary of responses"""
    dictionary: dict[str, int] = dict()
    fav_color: str = ""
    for key in responses:
        if responses[key] in dictionary:
            dictionary[f"{responses[key]}"] += 1
        else:
            dictionary[f"{responses[key]}"] = 1
    tally: int = 0
    for key2 in dictionary:
        if dictionary[key2] > tally:
            tally = dictionary[key2]
            fav_color = f"{key2}"
    return fav_color


def count(list1: list[str]) -> dict[str, int]:
    """Returns a dictionary of the count of each item in the input list"""
    result: dict[str, int] = {}
    for words in range(0, len(list1)):
        if list1[words] in result:
            result[list1[words]] += 1
        else:
            result[list1[words]] = 1
    return result


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for x in range(0, len(list1)):
        first_char = list1[x][0].lower()
        if first_char in result:
            result[first_char].append(list1[x])
        else:
            result[first_char] = [list1[x]]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Modifies a dictionary by making changes based on if students attend class or not"""
    day_check: bool = False
    for key in attendance:
        if day == key:
            day_check = True
    if day_check is False:
        attendance[f"{day}"] = list()
        # updates list of students who were present
    for key in attendance:
        people_list: list[str] = attendance[key]
        i: int = 0
        student_check: bool = False
        while (i < len(people_list)) and (student_check is not True):
            if student == people_list[i]:
                student_check = True
            else:
                i += 1
        if (student_check is False) and (day == key):
            people_list.append(student)
