# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
def make_str(size,a):
    s = '-'.join([chr(97 + x) for x in range(a,size)])
    return s[::-1]+s[1:]

def print_rangoli(size):
    for i in range(size-1,0,-1):
        # print('--'*i+make_str(size,i)+'--'*i)
        print(make_str(size,i).center(size*4-3,'-'))
    for i in range(size):
        # print('--'*i+make_str(size,i)+'--'*i)
        print(make_str(size,i).center(size*4-3,'-'))

print_rangoli(5)


