import math

def main():
    radialen = float(input("Voer het aantal radialen in: "))
    graden = radialenNaarGraden(radialen)
    minuten = gradenNaarTijd(graden)
    seconden = gradenNaarTijd(minuten)

    print(graden, minuten, seconden)

def radialenNaarGraden(radialen):
    graden = (180 / math.pi) * radialen
    return graden

def gradenNaarTijd(graden):
    minuten = (round(graden, 3) - int(graden)) * 60
    return minuten

main()
