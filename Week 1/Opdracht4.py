schaakbordLetters = ["a", "b", "c", "d", "e", "f", "g", "h"]
schaakbordCijfers = [1, 2, 3, 4, 5, 6, 7, 8]

def main():
    schaakbord = vulSchkaarbord()
    positiePaard = str(input("Voer de positie in waarin het paard zich nu begeeft: "))
    sprongPositie = str(input("Voer de positie in waar het paard naar toe wilt springen: "))

    print(bepaalMogelijkheidSprong(schaakbord, positiePaard, sprongPositie))

def vulSchkaarbord():
    schaakbord = {}
    position = 1
    for letter in schaakbordLetters:
        for cijfer in schaakbordCijfers:
            schaakbord[letter + str(cijfer)] = position
            position += 1
    return schaakbord

def bepaalMogelijkheidSprong(schaakbord, positie1, positie2):
    uitvoer = "Het paard kan{}springen van {} naar {}"
    verschil = (schaakbord[positie2] - schaakbord[positie1])

    if(verschil == 10 or verschil == 17):
        uitvoer = uitvoer.format(" ", positie1, positie2)
    else:
        uitvoer = uitvoer.format(" niet ", positie1, positie2)
    return uitvoer

main()