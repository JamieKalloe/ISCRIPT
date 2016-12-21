"""
Auteur - Jamie Kalloe, Michael van Kampen
"""
from datetime import timedelta, datetime

def main():
    print("{}".format(zomer_tijd(2013)))
    print("{}".format(zomer_tijd(2014)))
    print("{}".format(zomer_tijd(2015)))
    print("{}".format(winter_tijd(2013)))
    print("{}".format(winter_tijd(2014)))
    print("{}".format(winter_tijd(2015)))

    print(klok('27/06/2013'))
    print(klok('27/11/2013'))
    print(klok('31/03/2013'))
    print(klok('27/10/2013'))


def zomer_tijd(jaartal):
    datum = datetime(jaartal, 3, 31)
    weekDag = datum.weekday()

    while weekDag is not 6:
        datum -= timedelta(days=int(1))
        weekDag = datum.weekday()

    return datum


def winter_tijd(jaartal):
    datum = datetime(jaartal, 10, 31)
    weekdag = datum.weekday()

    while weekdag is not 6:
        datum -= timedelta(days=int(1))
        weekdag = datum.weekday()

    return datum


def klok(datum):
    dag = datetime.strptime(datum, '%d/%m/%Y')
    zomerTijd = zomer_tijd(dag.year)
    winterTijd = winter_tijd(dag.year)

    if dag > zomerTijd and dag < winterTijd:
        return "zomertijd"
    if dag > winterTijd:
        return "wintertijd"
    if dag == zomerTijd:
        return "Overschakeling van wintertijd naar zomertijd"
    if dag == winterTijd:
        return "Overschakeling van zomertijd naar wintertijd"

main()