"""Practice with defining variables and elif function"""

money: str = " dollars"

cost: int = 5

print("This sandwhich costs " + str(cost) + money)

cost: int = 7

print("This sandwhich now costs " + str(cost) + money)


def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price

def weather_report() -> str:
    weather: str= input("What is the weather?")
    if weather= "Rainy" or weather="Cold":
        print("This weather sucks!")
    elif weather= "Hot":
        print("Wow, its hot!")
    else:
        print("I don't recgonize this weather...")
    return weather

weather_report(Hot)    