from itertools import tee, islice, chain

generatie = [[True] + [False] * 7 for cel in range(6)]

def main():
    toonGeneratie(generatie)
    print(aantalBuren(generatie, 0, 0))
    print(aantalBuren(generatie, 1, 1))
    print(aantalBuren(generatie, 2, 2))

    volgende = volgendeGeneratie(generatie)
    toonGeneratie(volgende)

def toonGeneratie(generatie):
    for rij in generatie:
        waarde = ""
        for cel in rij:
            waarde += "X " if cel else "O "
        print(waarde)

def aantalBuren(generatie, rij, kolom):
    levendeBuren = 0
    rijen = [rij - 1, rij, rij + 1]

    for r in rijen:
        if r >= 0 and r < len(generatie):
            generatieRij = generatie[r]
            vorige, huidige, volgende = tee(generatieRij, 3)
            vorige = chain([None], vorige)
            volgende = chain(islice(volgende, 1, None), [None])
            cel = list(zip(vorige, huidige, volgende))
            for waarde in cel[kolom]:
                levendeBuren += 1 if waarde and waarde is not None else 0
        else:
            levendeBuren -= 1

    return levendeBuren if levendeBuren > 0 else 0


def volgendeGeneratie(generatie):
    volgende = []
    r = 0
    k = 0
    for rij in generatie:
        volgendeRij = []
        for cel in rij:
            buren = aantalBuren(generatie, r, k)
            cel = True if buren is 2 or 3 else cel
            cel = True if buren is 3 and cel is False else cel
            cel = False if buren < 2 else cel
            cel = False if buren >= 4 else cel
            volgendeRij.append(cel)
            k += 1
        volgende.append(volgendeRij)
        r += 1
        k = 0
    return volgende

main()