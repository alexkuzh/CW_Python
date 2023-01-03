# https://www.codewars.com/kata/6255e6f2c53cc9001e5ef629/train/python


# wordlist = {'SKIDS', 'RINSE', 'DEUCE', 'ALWAY', 'QUAIL', 'BANJO', 'BLADE', 'SKAGS', 'ALULA', 'METRO', 'SKALD', 'WATCH', 'SIZES', 'TIGHT', 'TEPEE', 'GRAIL', 'SKANK', 'ALOOS', 'SKEGG', 'GIRLY', 'MOVIE', 'KAYAK', 'ALLOT', 'RUPEE', 'TRUCK', 'SLOSH', 'SIZEL', 'CLOTH', 'LEECH', 'SMELT', 'SWEET', 'SIXTE', 'SKELF', 'COUPE', 'SKERS', 'CAULK', 'SHEEP', 'TANGO', 'TODAY', 'SKELL', 'BIDDY', 'TACIT', 'BISON', 'DROIT', 'SKAIL', 'ZONAL', 'MILKY', 'ALOIN', 'BRINE', 'BRUNT', 'CABAL', 'SKEED', 'SKEOS', 'VIRUS', 'PAYEE', 'SISTS', 'WOOLY', 'SIXER', 'GRAND', 'TROVE', 'SKEAN', 'SIZAR', 'SKEWS', 'SISTA', 'NASTY', 'CAGEY', 'HOARD', 'CLOUD', 'GUISE', 'FOCUS', 'BLOKE', 'VIVID', 'CHANT', 'CURRY', 'SKELM', 'WELCH', 'CLONE', 'SKEES', 'ALOED', 'BONEY', 'GEESE', 'MOWER', 'GLAZE', 'SKEET', 'MAUVE', 'DRAPE', 'RALPH', 'ALMUG', 'AXION', 'YACHT', 'CHOKE', 'SKIEY', 'STATE', 'PECAN', 'ALOHA', 'AMAHS', 'ALMUD', 'FLASK', 'DODGE', 'SITES', 'SKENS', 'SKETS', 'ABHOR', 'GRASP', 'SIXMO', 'SAUTE', 'SKEDS', 'SANDY', 'LAPSE', 'SHAKE', 'ALODS', 'MIRTH', 'SKATS', 'SITHE', 'ALLOW', 'SKEAR', 'SKEPS', 'FLUNG', 'MONTH', 'SERIF', 'ALVAR', 'SKEGS', 'SKATT', 'SKEEF', 'CHAIN', 'OCCUR', 'AMAIN', 'ALUMS', 'ALOES', 'SPILL', 'BEZEL', 'SITUS', 'SPANK', 'THEIR', 'SITUP', 'SIVER', 'FIFTH', 'ALTOS', 'SITED', 'KINKY', 'MOURN', 'ALTHO', 'TESTY', 'SWILL', 'CURVY', 'SKEEN', 'SKART', 'SKAWS', 'SKEIN', 'GRIMY', 'TENTH', 'FULLY', 'BASTE', 'SKIES', 'SIZER', 'SMITH', 'GRAFT', 'SKENE', 'FRIED', 'OTHER', 'TEASE', 'SKEER', 'ENDOW', 'SKELP', 'SIXES', 'PURGE', 'CLOSE', 'CATER', 'SIZED', 'THORN', 'AHEAD', 'HEDGE', 'RENEW', 'ALURE', 'MISER', 'SKIED', 'SWASH', 'SITKA', 'SITAR', 'ALOWE'}

wordlist = {'SKIDS','SKEET', 'SKETS', 'RINSE', 'SWEET'}
guesses = [('SPOIL', 'G----'), ('STEAD', 'GYG--'), ('SEETH', 'GYGY-')]

def wordle(wordlist, guesses):
    positive = {}
    unknown = {}
    r = set()
    for g in guesses:
        for i in range(len(g[0])):
            if g[1][i] == 'G':
                positive[i] = g[0][i]

    for g in guesses:
        a = set()
        for i in range(len(g[0])):
            if g[1][i] == 'Y':
                for x in range(len(g[0])):
                    if x not in positive.keys():
                        a.add(x)
                        unknown[g[0][i]] = a

    print(positive,unknown)
    for w in wordlist:
        flag = True
        for g in guesses:
            for l in range(len(g[1])):
                if g[1][l] == 'G':
                    if w[l] == positive[l]:
                        continue
                    else:
                        flag = False
                # if g[1][l] == 'Y':
                #     for m,n in unknown.items():
                #         if w.index()
                #
                #     if l in set('' or unknown.get(w[l])):
                #         continue
                #     else:
                #         flag = False
                if g[1][l] == '-':
                    if g[0][l] not in w:
                        continue
                    else:
                        flag = False
        if flag:
            r.add(w)
            # print(w,word,g)


    return r



u = {}
print(wordle(wordlist,guesses))
# print(set('' or u.get(0)))