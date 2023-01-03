# https://www.codewars.com/kata/628e3ee2e1daf90030239e8a/train/python
def interlockable(a, b):
    #return not (a^b < max(a,b))

    # short solution # return not(a&b)

    l = len(str(bin(max(a,b)))[2:])
    ast = str(bin(a))[2:]
    bst = str(bin(b))[2:]
    #
    print(ast.zfill(l))
    print(bst.zfill(l))
    print(str(bin(a & b))[2:])
    while min(a,b)>0:
        if a%2 and b%2:
            return False
        else:
            a = a >> 1
            b = b >> 1
            # print(a,b)
    return True

a = 9
b = 4

print(interlockable(a,b))
