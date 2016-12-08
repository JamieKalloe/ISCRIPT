
def main():
    patroon = []
    while True:
        invoer = input()
        if invoer == "":
            break
        patroon.append(invoer)

    for string in patroon:
        print("{}".format(string + string[::-1]))

main()