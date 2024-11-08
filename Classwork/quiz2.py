"""making sure i know how to do everything for the quiz"""

sample_list: list[int] = [1, 2, 3]

sample_list[0] = 0

# print(sample_list)


x: list[int] = [9, -1, 8, 5]
y: list[str] = ["cat", "dog", "fish"]

i = 0
while len(x) > i:
    print(x[i])
    i += 1

for vals in y:
    print(vals)


for index in range(0, len(x)):
    print(x[index])


my_dict: dict[int, str] = {8: "eight", 0: "zero", 3: "three", -1: "negative one"}


my_dict.pop(3)
cat = my_dict[0]

print(cat)
