# (line 2 and line 3 are examples of running an existing function
# from random import randint
# print(randint(1, 7))


# Function Definition
def sum(num1: int, num2: int) -> int:
    """Returns the sum of two integers"""
    return num1 + num2


print(sum(num1=11, num2=7))

def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg

def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon

print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))