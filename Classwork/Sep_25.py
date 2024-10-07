def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(msg[idx])
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"

chars(msg=a)


def assess(q:int, r:int) -> None:
    s: float = 0.0
    r=r+1
    if q % r == 0:
        s = q/r
    else:
        s = s + 4.0
    print(s)

assess(q=2, r=1)