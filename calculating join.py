import math
def calculating_Join():
    A = float(input("enter coordinate of Y2:"))
    B = float(input("enter coordinate of Y1:"))
    C = A - B
    print(C)
    D = float(input("enter coodinate of X2:"))
    E = float(input("enter coodinate of X1:"))
    F = D - E
    print(F)
    Distance =(math.sqrt((C ** 2) + (F ** 2)))# distance in metres
    print(Distance)
    Direction = math.degrees(math.tanh(C / F))# Direction in degrees minutes and seconds
    print(Direction)
    if C > 0 and F > 0:
        print(Direction)
    elif C < 0 and F < 0:
        print(Direction + 180.0)
    if C > 0 and F < 0:
        print(180.0 - Direction)
    else:
        print(Direction + 360.0)
calculating_Join()
