# https://www.codewars.com/kata/568f2d5762282da21d000011/train/python
import itertools

def gta(limit, *args): # find the base_list first
    #your code here    # I can't get out of my mind these words "Round Robin"
    lists = [list(str(item)) for item in args]
    s = []
    control = set()
    for i in range(max(len(l) for l in lists)):
        for k in range(len(lists)):
            if i < len(lists[k]) and int(lists[k][i]) not in control:
                s.append(int(lists[k][i]))
                control.add(int(lists[k][i]))
    s = s[:limit]
    acc = 0
    for m in range(limit):
        acc += sum(sum(i) for i in list(itertools.permutations(s, m+1)))
    return acc


print(gta(8, 12348, 47, 3639))
