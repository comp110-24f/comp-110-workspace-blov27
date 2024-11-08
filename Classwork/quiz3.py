"""Practice for quiz 3"""

my_dictionary: dict[str, float] = {}


msg: dict[str, int] = {"Hello": 1, "Yall": 2}
msg["Yall"] += 3
# print(msg["Yall"])


ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
# ids.pop(100)

# print(len(ids))


inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}

inventory["markers"] = 15

# print(inventory)

prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}
prices["milk"] = 2.50


scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
# for x in scores:
# print(x)
total_score = 0


my_list: list[int] = list()
my_list.append(8)
my_list.append(0)
my_list.append(3)
my_list.append(-1)

my_list.pop(2)
# print(my_list)

dog = my_list[2]

my_list[0] = 0
# print(my_list)

my_dict: dict[int, str] = dict()
my_dict[0] = "zero"
my_dict[1] = "one"
my_dict[-3] = "negative three"

my_dict.pop(-3)

cat = my_dict[0]


class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, make: str, model: str, year: int, color: str, mileage: float):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def updade_mileage(self, miles: float):
        self.mileage += miles


my_car = Car("hundai", "sonata", 2011, "silver", 110000)

print(my_car.color)

my_car.updade_mileage(120000)

print(my_car.mileage)


class Order:
    drink: str
    app: str
    meal: str
    price: float

    def __init__(self, drink: str, app: str, meal: str, price: float):
        self.drink = drink
        self.app = app
        self.meal = meal
        self.price = price

    def update_price(self, val_to_add):
        self.price += val_to_add


my_order = Order("water", "egg roll", "general tso", 12.09)
my_order.update_price(1.00)
print(my_order.price)

print(
    f"I ordered {my_order.drink} , {my_order.app} , and {my_order.meal} , and it cost {my_order.price} ."
)
