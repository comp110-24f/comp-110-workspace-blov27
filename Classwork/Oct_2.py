a: list[int] = [2, 4]
b: list[int] = a

a.append(6)
print(b)


def display(vals: list[int]) -> None:
    idx: int = 0
    while idx < len(vals):
        print(vals[idx])
        idx += 1


display((1, 2, 3, 4))

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0

print(x)
print(y)
