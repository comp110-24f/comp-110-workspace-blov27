"""Practice with for statements"""

vars: list[str] = ["x", "y", "z"]
new_list: list[str] = []

for elem in vars:
    # cycles through each item in list 'vars'
    new_list.append(elem)
# print(new_list)


pets: list[str] = ["Louie", "Bo", "Bear"]

for elem in pets:
    print(f"Good boy, {elem}!")
