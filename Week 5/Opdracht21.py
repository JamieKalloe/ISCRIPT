
def main():
    print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', '*'))
    print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '.'))
    print(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+'))

    rooster = '''rnbqkbnr
    pppppppp
    ********
    ********
    ********
    ********
    PPPPPPPP
    RNBQKBNR'''

    print(grid2fen(rooster))
    print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')))
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '.'), '.'))
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', '+'), '+'))

def fen2grid(fen, separator="*"):
    fen2 = ""
    for character in fen.split('/'):
        for letter in character:
            fen2 += letter if letter.isalpha() else int(letter) * separator
        fen2 += "\n"
    return fen2

def grid2fen(rooster, sepatator="*"):
    rooster = rooster.replace(" ", "").split('\n')
    rooster = [x for x in rooster if x is not '']
    output = ""
    for character in rooster:
        if all(character.isalpha() for letter in character):
            output += character
        else:
            n = 0
            for letter in character:
                n += 1 if not letter.isalpha() else 0
                output += str(n) + letter if letter.isalpha() and n > 0 else letter if letter.isalpha() else ""
                n = 0 if letter.isalpha() else n
            output += str(n) if n > 0 else ""
            n = 0

        output += "/" if character is not rooster[len(rooster) - 1] else ""

    return output

main()