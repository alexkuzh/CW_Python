# https://www.codewars.com/kata/645e541f3e6c2c0038a01216/train/python

def is_valid_train_arrangement(before, after):
    a1 = [(i,v) for i,v in enumerate(before) if v == '>']
    a2 = [(i, v) for i, v in enumerate(after) if v == '>']
    b1 = [(i,v) for i,v in enumerate(before) if v == '<']
    b2 = [(i, v) for i, v in enumerate(after) if v == '<']

    if len(before) != len(after) or \
            before.count('>') != after.count('>') or \
            before.count('<') != after.count('<'):
        return False
    for i in range(len(a1)):
        if a1[i][0]>a2[i][0]:
            return False
    for i in range(len(b1)):
        if b1[i][0]<b2[i][0]:
            return False
    for i in range(min(len(b1), len(a1))):
        if a2[i][0] - a1[i][0] >= b1[i][0] and \
                b1[i][0] - b2[i][0] >= a1[i][0]:
            return False

    for i in range(len(before)):
        if before[i] == '>' and after[i] == '<' or before[i] == '<' and after[i] == '>':
            return False

    print(a1)
    print(b1)
    print(a2)
    print(b2)
    return True


print(is_valid_train_arrangement("<>..<>", "<..<>>"))
# print(is_valid_train_arrangement(".<>...", "<....>"))
# print(is_valid_train_arrangement(">>.>..>>..................<.<>>>>>>.>.>.<..<<<<<<<<<<<<<.>>>>..>>.>.....<<<<<<<<<<<<<<<<<<",
#                                  "<<<<<<<<<<<<<<<<<<.>>.>.>..>.>..>.<.<<.<<<<<<<<<<<>>>>>>..>.>.......<<....>>...>>>........"))