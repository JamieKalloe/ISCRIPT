from datetime import timedelta

def main():
    soliDays = int(input("Voer de hoeveelheid sols in: "))
    print(solToDay(soliDays))

def solToDay(sol):
    """Returns the amount of earth days, converted from the given sol days."""
    return timedelta(hours=24, minutes=39, seconds=35.24409) * sol

main()
