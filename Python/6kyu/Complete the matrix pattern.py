# https://www.codewars.com/kata/582c01ad3fd1cc5736000348/train/python

def make_matrix(k: int, n: int) -> str:
    m = [[0] * n for i in range(n)]
    s = str(k)
    for y in range(n//2):
        for x in range(y+1,n-y-1):
            m[y][x] = s[1]
            m[n-y-1][x] = s[2]
        for x in range(y+1,n-y-1):
            m[x][y] = s[3]
            m[x][n-y-1] = s[4]
    for x in range(n):
        m[x][x] = s[0]
        m[x][n-x-1] = s[0]

    # for x in range(n):
    #     print(m[x])
    return '\n'.join([' '.join(m[x]) for x in range(n)])


print(make_matrix(13579, 7))
