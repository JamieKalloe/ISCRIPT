import random

buzz1 = ('integrated', 'total', 'systematized', 'parallel', 'functional', 'responsive', 'optional', 'synchronized', 'compatible', 'balanced')
buzz2 = ('management', 'organizational', 'monitored', 'reciprocal', 'digital', 'logistical', 'transitional', 'incremental', 'third-generation', 'policy')
buzz3 = ('options', 'flexibility', 'capability', 'mobility', 'programming', 'concept', 'time-phase', 'projection', 'hardware', 'contingency')

shakespeare1 = ['Thou']
shakespeare2 = ['artless', 'bawdy', 'beslubbering', 'bootless', 'churlish', 'cockered', 'clouted', 'craven', 'currish', 'dankish', 'dissembling', 'droning', 'errant', 'fawning', 'fobbing', 'froward', 'frothy', 'gleeking', 'goatish', 'gorbellied', 'impertinent', 'infectious', 'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled', 'mewling', 'paunchy', 'pribbling', 'puking', 'puny', 'quailing', 'rank', 'reeky', 'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly', 'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous', 'warped', 'wayward', 'weedy', 'yeasty']
shakespeare3 = ['base-court', 'bat-fowling', 'beef-witted', 'beetle-headed', 'boil-brained', 'clapper-clawed', 'clay-brained', 'common-kissing', 'crook-pated', 'dismal-dreaming', 'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing', 'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed', 'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged', 'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born', 'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured', 'knotty-pated', 'milk-livered', 'motley-minded', 'onion-eyed', 'plume-plucked', 'pottle-deep', 'pox-marked', 'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed', 'shard-borne', 'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited', 'tickle-brained', 'toad-spotted', 'urchin-snouted', 'weather-bitten']
shakespeare4 = ['apple-john', 'baggage', 'barnacle', 'bladder', 'boar-pig', 'bugbear', 'bum-bailey', 'canker-blossom', 'clack-dish', 'clotpole', 'coxcomb', 'codpiece', 'death-token', 'dewberry', 'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker', 'fustilarian', 'giglet', 'gudgeon', 'haggard', 'harpy', 'hedge-pig', 'horn-beast', 'hugger-mugger', 'jolthead', 'lewdster', 'lout', 'maggot-pie', 'malt-worm', 'mammet', 'measle', 'minnow', 'miscreant', 'moldwarp', 'mumble-news', 'nut-hook', 'pigeon-egg', 'pignut', 'puttock', 'pumpion', 'ratsbane', 'scut', 'skainsmate', 'strumpet', 'varlet', 'vassal', 'whey-face', 'wagtail']

def main():
    print(zoemzin1((buzz1, buzz2, buzz3)))
    print(zoemzin1([shakespeare1, shakespeare2, shakespeare3, shakespeare4]))
    print(zoemzin2(buzz1, buzz2, buzz3))
    print(zoemzin2(shakespeare1, shakespeare2, shakespeare3, shakespeare4))

def zoemzin1(buzzWoordenLijsten):
    zoemzin = ""
    for woordenLijst in buzzWoordenLijsten:
        zoemzin += woordenLijst[random.randrange(len(woordenLijst))] + " "
    return zoemzin

def zoemzin2(*buzzwoordenLijsten):
    zoemzin = ""
    for woordenLijst in buzzwoordenLijsten:
        zoemzin += woordenLijst[random.randrange(len(woordenLijst))] + " "
    return zoemzin

main()