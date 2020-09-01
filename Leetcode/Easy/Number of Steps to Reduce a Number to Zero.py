# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
def numberOfSteps(num):
    # s = bin(num)[2:]
    # return s.count('1')*2 - 1 + s.count('0')
    r = 0
    if num == 0: return 0
    while num>=0:
        if num%2 == 1:
            r +=2
        else:
            r+=1
        num = num >> 1
    return r-1

print(numberOfSteps(14))
