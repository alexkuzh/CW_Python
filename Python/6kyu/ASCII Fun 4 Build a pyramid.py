# https://www.codewars.com/kata/594a5d8f704e4d5561000019/train/python
def build_pyramid(string ,n):
    r = ''
    for i in range(1,n+1):
        r += ' '*((n-i)*len(string)//2)+''.join([x*i for x in list(string)])+'\n'
    print(r)
    print('fff')
    return r.rstrip()


print(build_pyramid('00-00..00-00',3))

