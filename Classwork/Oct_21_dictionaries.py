"""Examples of dictonary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# syntax for appending a dictionary
ice_cream["mint"] = 32

len(ice_cream)  # returns number of keys in dictonary

ice_cream.pop("strawberry")  # removes an item from the dictonary


# to iterate through every key in a loop, use for in


for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")
