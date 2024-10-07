def get_coords(xs: str, ys: str) -> None:
    xcount: int = 0
    ycount: int = 0
    while len(xs) > xcount:
        while len(ys) > ycount:
            print("(" + str(xs[xcount]) + "," + str(ys[ycount]) + ")")
            ycount += 1
        xcount += 1
        ycount = 0
