
def main():
    patroon = []
    while True:
        i = input()
        if i == "":
            break
        patroon.append(i)

    for s in patroon:
        print("{}".format(s + s[::-1]))

main()