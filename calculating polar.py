import math
def calculating_polar():
    M = float(input("entet first Y point coordinate:"))
    N = float(input("enter first X point coordinate:"))
    O = float(input("enter distance between the points:"))
    P = float(input("enter direction between 2 points:"))
    y = M + O*math.sin(P)
    x = N + O*math.cos(P)
    print(y)
    print(x)
calculating_polar()
