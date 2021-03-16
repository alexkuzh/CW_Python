# https://www.hackerrank.com/challenges/cut-the-sticks/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def cutTheSticks(arr):
    r = []
    arr.sort()
    while arr[0] != arr[-1]:
        r.append(len(arr))
        arr = [x-arr[0] for x in arr if x > arr[0]]
    r.append(len(arr))
    return r

s = '5 4 4 2 2 8'
q = list(map(int, s.rstrip().split(' ')))
print(cutTheSticks(q))

