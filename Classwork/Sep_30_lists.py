"""Practice with lists syntax"""

my_numbers: list[float] = []  # literal

extra_numbers: list[float] = list()  # constructor


my_numbers.append(7)
my_numbers.append(1.4)

# print(my_numbers)

grocery_list: list[str] = ["bananas", "milk", "bread"]

grocery_list[1] = "frozen pizza"
# print(grocery_list)


game_points: list[int] = [100, 112, 108]
# print(game_points)

game_points.append(94)  # adds a new item to the list
game_points[1] = 113  # changes an existing item in the list
game_points.pop(0)  # removes an item from the list
# print(game_points)


# getting the length of a list
# print("There are " + str(len(game_points)) + " items in the list 'game points'")


def display(values: list[int]) -> None:
    count: int = 0
    while count < len(values):
        print(values[count])
        count += 1


display(game_points)
