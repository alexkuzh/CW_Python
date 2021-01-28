# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    # r = ''
    # for x in s:
    #     if x.islower():
    #         r += x.upper()
    #     else:
    #         r += x.lower()
    # return r
    return ''.join([x.upper() if x.islower() else x.lower() for x in s])

print(swap_case(input()))
