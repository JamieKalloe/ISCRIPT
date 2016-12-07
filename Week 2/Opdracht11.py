import re

def main():
    wachtwoorden = []
    t = int(input("Geef het aantal testgevallen op: "))
    for testgeval in range(0, t):
        wachtwoorden.append(str(input("Voer wachtwoord {} in: ".format(testgeval))))

    veiligheidWachtwoorden = checkVeiligheid(wachtwoorden)
    for veiligheid in veiligheidWachtwoorden:
        print(veiligheid)

def checkVeiligheid(wachtwoorden):
    check = 0
    veiligheidWachtwoorden = []
    for wachtwoord in wachtwoorden:
        if len(wachtwoord) >= 8:
            check += 1
        if bool(re.search(wachtwoord, "?!^.*[A-Z]{2,}.*$)^[A-Za-z]*$")):
            check += 1
        if bool(re.search(wachtwoord, "?=.*[a-z]")):
            check += 1
        if any(char.isdigit() for char in wachtwoord):
            check += 1
        if bool(re.search(wachtwoord, "[$&+,:;=?@#|'<>.^*()%!-]")):
            check += 1

        veiligheid = "matig" if check > 3 else "zwak"
        veiligheid = "sterk" if check == 5 else "zwak"
        veiligheidWachtwoorden.append(veiligheid)

    return veiligheidWachtwoorden
main()