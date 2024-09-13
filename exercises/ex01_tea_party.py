"""Code that helps plan a tea party for me and my friends!"""

__author__: str = "730646728"
# identifies this file as being unique to me and my PID


def main_planner(guests: int) -> None:
    """Serves as a composite of the other three functions"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# the main_planner function is essential to running this program. It is a combination of the smaller 3 functions used and is a useful way to call all 3 functions
# i don't know why lines 12-17 couldn't all be on one line- i tried to contain them to one line but python kept adjusting my code after i ran it in the trailhead.


def tea_bags(people: int) -> int:
    """Determines how many tea bags will be needed for the party"""
    return people * 2


# I thought that this function and the corresponding 2 functions were pretty easy to make


def treats(people: int) -> int:
    """Determines how many treats will be needed for the party"""
    return int(tea_bags(people=people) * 1.5)


# I followed the same process that I used with the above function for making this next function
def cost(tea_count: int, treat_count: int) -> float:
    """Calculates cost of the tea party based on the tea count and treat count"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# I copied this function from the assignment instructions. It allows the program to be runnable.
