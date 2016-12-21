import random

def main():
    print(gebeuren_samen(6, 3))
    print(gebeuren_samen(6, 3))
    print(schat_kans(6, 2, 10000))
    print(schat_kans(365, 23, 10000))

def gebeuren_samen(m ,n):
    gebeurtenissen = [0] * m

    for testgeval in range(0, n):
        gebeurtenissen[random.randrange(m)] += 1

    return any(gebeurtenis > 1 for gebeurtenis in gebeurtenissen)

def schat_kans(m, n, cases):
    kans = 0.0

    for gebeurtenis in range(0, cases):
        if(gebeuren_samen(m, n)):
            kans += 1

    return kans / cases

main()