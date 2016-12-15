"""
Auteur - Jamie Kalloe, Michael van Kampen
"""
from functools import reduce
from itertools import cycle

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    encrypt_code = codeer('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS')
    print("{}".format(encrypt_code))
    print("{}".format(decrypt('CIRCUS', encrypt_code)))
    encrypt_code = codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR')
    print("{}".format(encrypt_code))
    print("{}".format(decrypt('ARTHUR', encrypt_code)))


def codeer(bericht, sleutel):
    paren = zip(bericht, cycle(sleutel))
    gecodeerdBericht = ""

    for paar in paren:
        if paar[0].isupper():
            totaal = reduce(lambda berichtLetter, sleutelLetter: ALPHA.index(berichtLetter) + ALPHA.index(sleutelLetter), paar)
            gecodeerdBericht += ALPHA[totaal % 26]
        else:
            gecodeerdBericht += paar[0]

    return gecodeerdBericht


def decrypt(sleutel, bericht):
    paren = zip(bericht, cycle(sleutel))
    resultaat = ''

    for paar in paren:
        if paar[0].isupper():
            totaal = reduce(lambda berichtLetter, sleutelLetter: ALPHA.index(berichtLetter) - ALPHA.index(sleutelLetter), paar)
            resultaat += ALPHA[totaal % 26]
        else:
            resultaat += paar[0]

    return resultaat

main()
