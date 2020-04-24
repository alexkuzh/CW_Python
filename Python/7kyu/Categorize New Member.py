def openOrSenior(data):
    # Hmmm.. Where to start?
    a = []
    for x in data:
        if x[0]>=55 and x[1] > 7:
            a.append('Senior')
        else:
            a.append('Open')
    return a

print(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]))