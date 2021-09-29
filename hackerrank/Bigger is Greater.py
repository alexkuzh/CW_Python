# https://www.hackerrank.com/challenges/bigger-is-greater/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def biggerIsGreater(w):
    l = list(w)
    for i in range(1,len(w)+1):
        if l[-i]>l[-i-1]:
            l[-i],l[-i-1] = l[-i-1],l[-i]
            if ''.join(l) > w:
                return ''.join(l)
    return 'no answer'


print(biggerIsGreater('dkhc'))
# hcdk
