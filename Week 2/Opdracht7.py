def main():
    testgevallen = []

    t = int(input("Voer een aantal testgevallen in:"))

    if t > 50:
        exit(-1)

    while len(testgevallen) < t:
        x = input()
        if x == "":
            break

        x = int(x)
        if 0 > x > 100: exit(-1)
        testgevallen.append(int(x))

    for getal in testgevallen:
        print(sum(getal, 10000))


def sum(n, y):
    test_geval = n
    while test_geval <= y:
        tmp = test_geval
        if sum_digit(tmp) == n:
            return test_geval
        test_geval += n
    return -1


def sum_digit(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

main()