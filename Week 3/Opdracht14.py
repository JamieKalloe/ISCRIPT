
def main():
    print(levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True))
    print(levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5, fastfood=True))
    print(levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0, fastfood=False))
    print(levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14, fastfood=True))
    print(levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4, fastfood=False))

def levensverwachting(geslacht, roker, sport, alcohol, fastfood):
    verwachting = 70
    verwachting += 4 if geslacht is "vrouw" else 0
    verwachting += 5 if roker is False else -5
    verwachting += sport if sport > 0 else -3
    verwachting += 2 if alcohol is 0 else -(alcohol - 7) / 2 if alcohol > 7 else 0
    verwachting += 3 if fastfood is False else 0

    return verwachting

main()