# https://www.codewars.com/kata/5616868c81a0f281e500005c/train/python

def rank(st, we, n):
    # your code
    # print(st,we,n)
    if st == '':
        return 'No participants'
    names = st.lower().split(',')
    if len(names) < len(we) or len(names) < n:
        return 'Not enough participants'
    # w = {}
    # for i in range(len(names)):
    #     w[names[i]] = sum([ord(c) - 95 for c in names[i]]) * we[i]
    # # q = sorted(sorted(w.items(), key=operator.itemgetter(0)), key=operator.itemgetter(1), reverse=True)[n-1][0]
    # q = sorted(sorted(w.items(), key=lambda a:a[0]), key=lambda a:a[1], reverse=True)[n-1][0]
    # return [x for x in st.split(',') if x.lower() == q][0]

    name_score = lambda names, w: w * (len(names) + sum([ord(c.lower()) - 96 for c in names]))
    print(name_score)
    scores = [name_score(s, we[i]) for i, s in enumerate(st.split(','))]
    print(scores)
    scores = list(zip(st.split(','), scores))
    print(scores)
    scores.sort(key=lambda x: (-x[1], x[0]))
    print(scores)
    return scores[n - 1][0]


# print(rank('Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden', [1, 3, 5, 5, 3, 6], 2))
print(rank('William,Willaim,Olivia,Olivai,Lily,Lyli', [1, 1, 1, 1, 1, 1], 1))
