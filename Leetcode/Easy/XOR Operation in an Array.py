# https://leetcode.com/problems/xor-operation-in-an-array/
# 1486

def xorOperation(n, start):
    a = []
    # x = 0
    for i in range(n):
        # a.append(str(start + 2*i))
        a.append(start + 2*i)
    # print('^'.join(a))
    x = a[0]
    for i in range(1,len(a)):
        x = x ^ a[i]
    return x
    # return eval('^'.join(a))


print(xorOperation(4,3))

print()