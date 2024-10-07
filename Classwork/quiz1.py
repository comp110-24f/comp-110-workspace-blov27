"""Practice reviewing for quiz 01"""

x: int = int(input("Pick a number: "))
y: int = 10
z: int = 2
x = x - 1
if x < 10:
    print("A")
else:
    if (x % z) == 0:
        print("B")
if x == (y + z):
    print("C")
else:
    print("D")


if 2 + 2 == 4:
    print("That makes sense")
else:
    print("Something is very wrong")

n: int = 1
while n < 1000:
    n = n + 1
    print(n)
