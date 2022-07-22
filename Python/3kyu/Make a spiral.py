# Make a snake
# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

def spiralize(size):
    d = [[0] * size for _ in range(size)]
    x,y = 0,-1
    U,R,D,L = 0,size,size,0

    for i in range(size):
        #right
        while y<size-1 and y<R and x>=U and x<=D:
            y += 1
            d[x][y] = 1

        U = x + 2

        #down
        while x<size-1 and x<D and y>=L and y<=R:
            x += 1
            d[x][y] = 1

        R = y - 2

        #left
        while y>0 and y>L and x>=U and x<=D:
            y -= 1
            d[x][y] = 1

        D = x - 2

        #up
        while x>0 and x >U and y>=L and y<=R:
            x -= 1
            d[x][y] = 1

        L = y + 2

    for x in d:
        print(x)
    return None


print(spiralize(13))