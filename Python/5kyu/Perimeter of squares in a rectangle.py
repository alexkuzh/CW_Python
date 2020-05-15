# https://www.codewars.com/kata/559a28007caad2ac4e000083/train/python
def fibo(n):
    a, b, c = 1, 1, 1
    for i in range(n - 1):
        a, b = b, a + b
        c += a
    return c

def perimeter(n):
    # your code
    return 4 * fibo(n+1)

print(perimeter(6))
