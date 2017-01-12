from math import radians, cos, sin, sqrt, atan2

"""
    Auteur - Jamie Kalloe, Michael van Kampen
"""

def main():
    luchthavens = leesLuchthavens("luchthavens.txt")
    print(luchthavens["ADK"])
    print(luchthavens["DCA"])
    print(luchthavens["4OM"])
    print(afstand('P60', 'MSN', luchthavens))
    print(afstand('ADK', 'DCA', luchthavens))
    print(tussenlanding('ADK', 'DCA', luchthavens, 4000))

def leesLuchthavens(bestand):
    luchthavens = {}
    with open(bestand) as text:
        next(text)
        for lijn in text:
            lijn = lijn.split('\t')
            lijn[4] = lijn[4].replace('\n', "")
            luchthavens[lijn[0][1:len(lijn[0]) - 1]] = list((lijn[1:len(lijn)]))

    return luchthavens


def afstand(luchthavenA, luchthavenB, luchthavens):
    straal = float(6372.795)

    b1, b2, l1, l2 = map(radians,
                         [float(luchthavens[luchthavenA][0]),
                          float(luchthavens[luchthavenB][0]),
                          float(luchthavens[luchthavenA][1]),
                          float(luchthavens[luchthavenB][1])])

    formuleA = sqrt((cos(b2) * sin(l1 - l2)) ** 2 + (cos(b1) * sin(b2) - (sin(b1) * cos(b2) * cos(l1 - l2))) ** 2)
    formuleB = ((sin(b1) * sin(b2)) + (cos(b1) * cos(b2) * cos(l1 - l2)))
    resultaat = straal * atan2(formuleA, formuleB)

    return resultaat


def tussenlanding(luchthavenA, luchthavenB, luchthavens, reikwijdte=4000):
    maximaleAfstand = 2 * reikwijdte

    if afstand(luchthavenA, luchthavenB, luchthavens) > reikwijdte:
        luchthavenC = ""
        for luchthaven in luchthavens:
            afstandA = afstand(luchthavenA, luchthaven, luchthavens)
            afstandB = afstand(luchthaven, luchthavenB, luchthavens)
            if afstandA < reikwijdte and reikwijdte > afstandB:
                afstandTot = afstandA + afstandB
                if afstandTot < maximaleAfstand:
                    maximaleAfstand = afstandTot
                    luchthavenC = luchthaven

        if not (maximaleAfstand == 2 * reikwijdte):
            return luchthavenC
        else:
            return None
    else:
        return None

main()