"""Practice with for statements"""

vars: list[str] = ["x", "y", "z"]
new_list: list[str] = []

for elem in vars:
    # cycles through each item in list 'vars'
    new_list.append(elem)
# print(new_list)


pets: list[str] = ["Louie", "Bo", "Bear"]

for animal in pets:
    print(f"Good boy, {animal}!")


for index in range(0, len(pets)):
    print(pets[index])


names: list[str] = ["Alyssa", "Janet", "Vanessa"]

for person in range(0, len(names)):
    print(f"{person}: {names[person]}")
