def spell(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index = index + 1


spell(msg="pineapple")
