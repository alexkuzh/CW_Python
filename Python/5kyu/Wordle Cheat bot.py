# https://www.codewars.com/kata/6255e6f2c53cc9001e5ef629/train/python


wordlist = {'SKIDS', 'RINSE', 'DEUCE', 'ALWAY', 'QUAIL', 'BANJO', 'BLADE', 'SKAGS', 'ALULA', 'METRO', 'SKALD', 'WATCH', 'SIZES', 'TIGHT', 'TEPEE', 'GRAIL', 'SKANK', 'ALOOS', 'SKEGG', 'GIRLY', 'MOVIE', 'KAYAK', 'ALLOT', 'RUPEE', 'TRUCK', 'SLOSH', 'SIZEL', 'CLOTH', 'LEECH', 'SMELT', 'SWEET', 'SIXTE', 'SKELF', 'COUPE', 'SKERS', 'CAULK', 'SHEEP', 'TANGO', 'TODAY', 'SKELL', 'BIDDY', 'TACIT', 'BISON', 'DROIT', 'SKAIL', 'ZONAL', 'MILKY', 'ALOIN', 'BRINE', 'BRUNT', 'CABAL', 'SKEED', 'SKEOS', 'VIRUS', 'PAYEE', 'SISTS', 'WOOLY', 'SIXER', 'GRAND', 'TROVE', 'SKEAN', 'SIZAR', 'SKEWS', 'SISTA', 'NASTY', 'CAGEY', 'HOARD', 'CLOUD', 'GUISE', 'FOCUS', 'BLOKE', 'VIVID', 'CHANT', 'CURRY', 'SKELM', 'WELCH', 'CLONE', 'SKEES', 'ALOED', 'BONEY', 'GEESE', 'MOWER', 'GLAZE', 'SKEET', 'MAUVE', 'DRAPE', 'RALPH', 'ALMUG', 'AXION', 'YACHT', 'CHOKE', 'SKIEY', 'STATE', 'PECAN', 'ALOHA', 'AMAHS', 'ALMUD', 'FLASK', 'DODGE', 'SITES', 'SKENS', 'SKETS', 'ABHOR', 'GRASP', 'SIXMO', 'SAUTE', 'SKEDS', 'SANDY', 'LAPSE', 'SHAKE', 'ALODS', 'MIRTH', 'SKATS', 'SITHE', 'ALLOW', 'SKEAR', 'SKEPS', 'FLUNG', 'MONTH', 'SERIF', 'ALVAR', 'SKEGS', 'SKATT', 'SKEEF', 'CHAIN', 'OCCUR', 'AMAIN', 'ALUMS', 'ALOES', 'SPILL', 'BEZEL', 'SITUS', 'SPANK', 'THEIR', 'SITUP', 'SIVER', 'FIFTH', 'ALTOS', 'SITED', 'KINKY', 'MOURN', 'ALTHO', 'TESTY', 'SWILL', 'CURVY', 'SKEEN', 'SKART', 'SKAWS', 'SKEIN', 'GRIMY', 'TENTH', 'FULLY', 'BASTE', 'SKIES', 'SIZER', 'SMITH', 'GRAFT', 'SKENE', 'FRIED', 'OTHER', 'TEASE', 'SKEER', 'ENDOW', 'SKELP', 'SIXES', 'PURGE', 'CLOSE', 'CATER', 'SIZED', 'THORN', 'AHEAD', 'HEDGE', 'RENEW', 'ALURE', 'MISER', 'SKIED', 'SWASH', 'SITKA', 'SITAR', 'ALOWE'}

guesses = [('SPOIL', 'G----'), ('STEAD', 'GYG--'), ('SEETH', 'GYGY-')]


def wordle(wordlist, guesses):
    # print(wordlist, guesses)
    # S_E__ TET not POILADH
    r = set()
    r1 = set()
    positive = {}
    unknown = {}
    for g in guesses:
        for i in range(len(g[0])):
            unknown[g[0][i]] = 0
    for g in guesses:
        for i in range(len(g[0])):
            if g[1][i] == '-':
                unknown[g[0][i]] -= 1
            if g[1][i] == 'G':
                positive[i] = g[0][i]
            elif g[1][i] == 'Y':
                unknown[g[0][i]] += 1

    for w in wordlist:
        flag = True
        for index,letter in positive.items():
            if w[index] != letter:
                flag = False
                break
        if flag:
            r.add(w)
    print(r)
    negative = set()
    for letter, coun in unknown.items():
        if coun<0:
            negative.add(letter)
    print(negative)
    for w in r:
        if len(set(w).intersection(negative))>0:
            continue
        r1.add(w)

    print(r1)
    r = r1.copy()
    r1.clear()
    yellow = set()
    for letter, coun in unknown.items():
        if coun>=0:
            yellow.add(letter)
    print(yellow)
    for w in r:
        if len(set(w).intersection(yellow))!=len(yellow):
            continue
        r1.add(w)


    print(positive,unknown)

    return r1

print(wordle(wordlist, guesses))

#{'RETALIATIONISTS'}

# a = set('SKEE')
# b = {'E', 'T'}
# print(f'a = {sorted(a)}\nb={sorted(b)}')
# print(sorted(a.intersection(b)))