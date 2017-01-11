
def main():
    opgave = 'Qmvrbwlf xwkd iopzlw vf zml pcwvfxzvyl.'
    oplossing = 'Ch?ld??? ??ow fas??r ?n ??? ?p?i?gt?me.'
    print(cryptogram(opgave, oplossing))

    opgave = 'Zhp suxobpuw sbmtkopw Nxwkdnx.'
    oplossing = '?h? p?n???a? ?rod?ces I???l??.'
    print(cryptogram(opgave, oplossing))

    opgave = 'Jujso ldmtq wyjqi tvadi ltek tq lads tw t wcqnej xjee.'
    oplossing = '?v?ry ??ma? ?p??? ?bout h??f ?? ???? ?s ? ??ng?e c?l?.'
    print(cryptogram(opgave, oplossing))

    opgave = "V atult'a amrdd qvl zr nrbrqbrn zx v wumvl v medr vivx."
    oplossing = "? ????k's ???l? ??n ?? ??t???ed ?y a hum?? ? ?i?? ?w??."
    print(cryptogram(opgave, oplossing))

def cryptogram(opgave, oplossing):
    juisteZin = list(oplossing)
    for oplossingKarakter in range(0, len(oplossing)):
        if oplossing[oplossingKarakter] is "?":
            for opgaveKarakter in range(0, len(opgave)):
                if opgave[oplossingKarakter].upper() == opgave[opgaveKarakter].upper():
                    if oplossing[opgaveKarakter] is not "?":
                        juisteZin[oplossingKarakter] = oplossing[opgaveKarakter]

    return "".join(juisteZin)

main()