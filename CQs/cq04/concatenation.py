def concat(msg1: str, msg2: str) -> str:
    return msg1 + msg2


word1: str = "happy"
word2: str = "tuesday"


def main() -> None:
    print(concat(word1, word2))


if __name__ == "__main__":
    main()
