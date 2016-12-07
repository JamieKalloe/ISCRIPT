import re

def main():
    print("palindroomzin" if isPalindroomZin("Er is daar nog onraad, Sire.") else "geen palindroomzin")

def isPalindroomZin(sentence):
    sentence = re.sub(r"[^A-Za-z]+", '', sentence).lower()
    for letter in range(0, len(sentence)):
        if sentence[letter] != sentence[::-1][letter]:
            return False
    return True

main()