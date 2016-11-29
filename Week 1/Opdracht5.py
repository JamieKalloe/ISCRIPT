import math

def main():
    x1 = float(input("Voer x1 in: "))
    y1 = float(input("Voer y1 in: "))
    x2 = float(input("Voer x2 in: "))
    y2 = float(input("Voer y2 in: "))
    x3 = float(input("Voer x3 in: "))
    y3 = float(input("Voer y3 in: "))

    voetpunt = berekenVoetpunt(x1, y1, x2, y2, x3, y3)
    afstand = berekenAfstand(voetpunt, x3, y3)
    zone = berekenZone(afstand)

    print('Voetpunt: {}'.format(voetpunt))
    print('Afstand: {}'.format(afstand))
    print('Zone: {}'.format(zone))

def berekenVoetpunt(x1, y1, x2, y2, x3, y3):
    u = ((x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)) / ((math.pow(x2 - x1, 2)) + math.pow(y2 - y1, 2))

    xv = x1 + u * (x2 - x1)
    yv = y1 + u * (y2 - y1)

    voetpunt = (xv, yv)
    return voetpunt

def berekenAfstand(voetpunt, x3, y3):
    xv, yv = voetpunt
    afstand = math.sqrt(math.pow(xv - x3, 2) + math.pow(yv - y3, 2))
    return afstand

def berekenZone(afstand):
    if 0 <= afstand <= 12:
        zone = "territoriale wateren"
    elif 12 < afstand <= 24:
        zone = "aansluitende zone"
    elif 24 < afstand <= 200:
        zone = "exclusieve economische zone"
    elif afstand > 200:
        zone = "internationale wateren"
    else:
        zone = "something went wrong"

    return zone

main()