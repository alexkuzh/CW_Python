# https://www.hackerrank.com/challenges/manasa-and-stones/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import itertools as i


def stones(n, a, b):
    return sorted(set(sum(x) for x in i.product([a, b], repeat=n-1)))


# print(list(i.product([1,2], repeat=3)))
result = stones(3, 1, 2)
print((' '.join(map(str, result))))