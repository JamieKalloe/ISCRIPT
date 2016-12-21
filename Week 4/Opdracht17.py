"""
Auteur - Jamie Kalloe, Michael van Kampen
"""
from iteration_utilities import grouper

prijzen = (3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23)


def main():
    print("{}".format(samen(prijzen)))
    l = groeperen(prijzen)
    print("{}".format(l))
    gegroepeerd(l)
    totaal_prijs = samen(prijzen)
    lagePrijs = gegroepeerd(l)
    verschil = totaal_prijs - lagePrijs
    print("{}".format(verschil))


def samen(prijzen):
    prijzen = sorted(prijzen, key=float)
    gratisProducten = int(len(prijzen) / 4)
    total = 0
    for prijs in prijzen:
        total += prijs

    for gratisProduct in range(0, gratisProducten):
        total -= prijzen[gratisProduct]

    return total


def groeperen(prijzen):
    prijzen = sorted(prijzen, key=float, reverse=True)
    return list(grouper(prijzen, 4))

def gegroepeerd(prijzen):
    totaal = 0
    for index in range(0, len(prijzen)):
        hoogsteIndex = len(prijzen[index]) - 1
        if hoogsteIndex == 3:
            totaal += sum(prijzen[index][0:len(prijzen[index]) - 1])
        else:
            totaal += sum(prijzen[index])

    return totaal

main()