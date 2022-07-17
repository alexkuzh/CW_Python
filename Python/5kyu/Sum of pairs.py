# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python
def sum_pairs(ints, s):
    ind = len(ints)
    a = None
    for i in range(len(ints)-1):
        for k in range(i+1,len(ints)):
            if ints[i]+ints[k] == s and ind>k:
                a = [ints[i],ints[k]]
                return a
                ind = k
                print(a)
    return a

def sum_pairs_1(ints, s):
    ind = len(ints)
    a = None
    for i in range(len(ints)-1):
        try:
            if ints[i+1:].index(s - ints[i])<ind:
                ind = ints.index(s - ints[i])
                a = [ints[i],ints[ind]]
                # print(a)
        except:
            pass
    return a

def sum_pairs_2(ints, s):
    a = set()
    for i in range(len(ints)):
        if s - ints[i] in a:
            return [s - ints[i],ints[i]]
        else:
            a.add(ints[i])
    return None

print(sum_pairs_2([1, 4, 8, 7, 3, 15],8))