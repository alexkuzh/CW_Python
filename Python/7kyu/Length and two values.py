# https://www.codewars.com/kata/62a611067274990047f431a8?utm_source=newsletter
def alternate(n, first_value, second_value):
    a = []
    for _ in range(n//2+1):
        a.append(first_value)
        a.append(second_value)
    return a[:n]