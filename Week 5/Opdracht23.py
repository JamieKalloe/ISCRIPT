import codecs

def main():
    print(prijzen('prijzen.csv', prijs='nobelprijs', jaar=1994))
    print(prijzen('prijzen.csv', prijs='nobelprijs', discipline='wiskunde'))
    print(prijzen('prijzen.csv', nationaliteit='bel'))
    print(prijzen('prijzen.csv', discipline='scheikunde', laureaten=3))
    print(prijzen('prijzen.csv', motivering='röntgen', discipline='natuurkunde', nationaliteit='GB'))

def prijzen(file, **argumenten):
    with codecs.open(file, 'r', encoding='utf8') as data:
        next(data)
        prijzen = [prijs.split(";") for prijs in data]

    for argument in sorted(argumenten):
        if argument is "discipline":
            prijzen = [prijs for prijs in prijzen if str(prijs[1]).upper() == str(argumenten.get(argument)).upper()]
        if argument is "jaar":
            prijzen = [prijs for prijs in prijzen if str(prijs[2]) == str(argumenten.get(argument))]
        if argument is "laureaten":
            prijzen = [prijs for prijs in prijzen if len(str(prijs[3]).split(",")) == int(argumenten.get(argument))]
        if argument is "motivering":
            prijzen = [prijs for prijs in prijzen if str(prijs[4]).upper().find(str(argumenten.get(argument)).upper()) > -1]
        if argument is "nationaliteit":
            prijzen = [prijs for prijs in prijzen if "(" + str(argumenten.get(argument)).upper() + ")" in str(prijs[3]).upper().replace(",", "").split(" ")]
        if argument is "prijs":
            prijzen = [prijs for prijs in prijzen if str(prijs[0]).upper() == str(argumenten.get(argument)).upper()]

    return prijzen

main()