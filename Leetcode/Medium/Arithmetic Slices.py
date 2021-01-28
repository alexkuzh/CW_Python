# 413
# https://leetcode.com/problems/arithmetic-slices/
def chekslis(l):
    d = l[1]-l[0]
    n = len(l)
    if (2*l[0]+d*(n-1))*n/2 == sum(l):
        return True
    return False

def numberOfArithmeticSlices1(l):
    a = []
    if len(l) <= 2:
        return 0
    for n in range(3, len(l)+1):
        for i in range(0, len(l) - n + 1):
            if chekslis(l[i:i + n]):
                a.append(l[i:i + n])
    return a

def numberOfArithmeticSlices(l):
    d = l[1]-l[0]
    k = 0
    m = 0
    # for i in range(1,len(l)):
    i = 1
    while i < len(l):
        if l[i]-l[i-1] == d:
            k+=1
        else:
            if k>=2:
                m += sum(range(k))
            k=0
            d = l[i]-l[i-1]
            i -=1
        i +=1
    return m

# print(chekslis([1, 2, 3,4,6]))
# print(numberOfArithmeticSlices1([1,2,3,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,8,10]))
# 6 = 4*3, 3*4, 2*5, 1*6
