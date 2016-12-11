
def main():
    print(decodeer('aoesifibolwkrdexeioayngoxxfhtslhtlx', 5))
    print(decodeer("aohpdntilirndsnefxxftgonomceexxrloewftmyex", 6))

def decodeer(bericht, kolommen):
    gedecodeerdBericht = [""] * kolommen
    omgekeerd = False
    for rij in range(0, len(bericht), kolommen):
        kolom = 0
        for letter in bericht[rij:(rij + kolommen)] if not omgekeerd else bericht[rij:(rij + kolommen)][::-1]:
            gedecodeerdBericht[kolom] += letter
            kolom += 1
        omgekeerd = not omgekeerd
    return "".join(gedecodeerdBericht)

main()