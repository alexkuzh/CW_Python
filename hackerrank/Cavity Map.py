# https://www.hackerrank.com/challenges/cavity-map/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def cavityMap(grid):
    a = []
    a.append(grid[0])
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            if str(grid[i][j]) > max(grid[i][j - 1], grid[i][j + 1], grid[i - 1][j], grid[i + 1][j]):
                grid[i] = grid[i].replace(grid[i][j], 'X')
        a.append(grid[i])
    a.append(grid[-1])
    return a


s = '462664\n669722\n297288\n796928\n584497\n357431'
n = 6
grid = s.split('\n')
for _ in grid:
    print(_)


a = cavityMap(grid)
print(a)
for _ in a:
    print(_)

'''
462664
66X722
297288
796X28
5844X7
357431
'''