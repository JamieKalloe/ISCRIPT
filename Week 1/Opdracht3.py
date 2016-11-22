import math


def main():
    x = float(input("Voer de x coordinaten in: "))
    y = float(input("Voer de y coordinaten in: "))
    r = straal(x, y)
    hoek0 = hoek(x, y)
    print("straal: ", r)
    print("hoek0: ", hoek0)

def straal(x, y):
    return math.sqrt((x * x) + (y * y))

def hoek(x, y):
    return math.atan(math.cos(x) / math.sin(y) if x or y != 0 else 0)

main()