import random

def main():
    gemiddeldeSalaris = berekenGemiddeldeSalarissen()

def berekenGemiddeldeSalarissen():
    salarissen = []
    totaal = 0

    eersteSalaris = float(input("Voer het eerste salaris in: "))
    willekeurigGetal = random.randint(10000, 1000000)
    salarissen.append(eersteSalaris + willekeurigGetal)
    totaal += eersteSalaris + willekeurigGetal
    vorigeSalaris = eersteSalaris
    print("Willekeurig getal: {}".format(willekeurigGetal))

    salaris = input()
    while salaris != "stop":
        totaal += float(salaris)
        salarissen.append(float(vorigeSalaris) + float(salaris))
        vorigeSalaris = float(salaris)
        salaris = input("Voer het salaris van een werknemer in: ")

    counter = 0
    for gemiddeldeSalaris in salarissen:
        gemiddelde = round((willekeurigGetal - gemiddeldeSalaris) / len(salarissen), 2)
        print("werknemer #{} fluistert €{}".format(counter + 1, gemiddelde))
        counter += 1
    print("gemiddelde: {}".format((totaal - willekeurigGetal) / len(salarissen)))
main()