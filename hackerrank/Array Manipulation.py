# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''Complete the function arrayManipulation in the editor below. It must return an integer,
the maximum value in the resulting array.
arrayManipulation has the following parameters:
n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.'''

def arrayManipulation(n, queries):
    #n, inputs = [int(n) for n in input().split(" ")]
    a = [0] * (n + 1)
    for i in queries:
        a[i[0]-1] += i[2]
        a[i[1]] -= i[2]
    max = x = 0
    for i in a:
        x = x + i
        if (max < x): max = x
    return max

'''
10 4
2 6 8
3 5 7
1 8 1
5 9 15    
'''
n = 10
queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5,9,15]]
print(arrayManipulation(n, queries))