from random import randint

print(randint(1, 7))




def add(num1:float, num2:float) -> float:
    """Adds two numbers"""
    return(num1+num2)

print(add(num1=2,num2=2))

def practice(word: str) -> None:
    print("This is my word: " + word + "!")

