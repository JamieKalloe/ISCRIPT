import math

def main():
    n = int(input("Voer het getal in"))
    berekenPythagoreesDrietal(n)

def berekenPythagoreesDrietal(n):
    for a in range(1, n):
        for b in range(a, n - a):
            c = math.sqrt(a ** 2 + b ** 2)

            if a + b + c == n:
                print("({} , {} , {})".format(a, b, c))

main()