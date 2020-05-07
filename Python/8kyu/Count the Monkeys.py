# https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python
def monkey_count(n):
# your code here
    a = []
    for x in range(1, n+1):
        a.append(x)
    return a

print(monkey_count(10))

# return [i+1 for i in range(n)]