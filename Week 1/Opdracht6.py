
def main():
    leeftijd = int(input("Voer de leeftijd van de patient (in maanden) in: "))
    chlorideconcentratie = int(input("Voer de gemeten chloriedeconcentratie (in mmol/L) in: "))

    leeftijdsgrens = berekenOuderJonger(leeftijd)
    berekendeChlorideconcentratie = berekenChlorideconcentratie(chlorideconcentratie, leeftijdsgrens)

    print(berekendeChlorideconcentratie)

def berekenOuderJonger(leeftijd):
    l = ""
    if leeftijd <= 6:
        l = "jonger"
    else:
        l = "ouder"
    return l

def berekenChlorideconcentratie(chlorideconcentratie, leeftijdsgrens):
    if leeftijdsgrens is "jonger":
        if chlorideconcentratie <= 29 :
            chloride = "CF is hoogst onwaarschijnlijk"
        elif 29 < chlorideconcentratie < 60:
            chloride = "CF is mogelijk"
        elif chlorideconcentratie >= 60 :
            chloride = "CF is waarschijnlijk"

    if leeftijdsgrens is "ouder":
        if chlorideconcentratie <= 39 :
            chloride = "CF is hoogst onwaarschijnlijk"
        elif 39 < chlorideconcentratie < 60:
            chloride = "CF is mogelijk"
        elif chlorideconcentratie >= 60:
            chloride = "CF is waarschijnlijk"

    return chloride

main()