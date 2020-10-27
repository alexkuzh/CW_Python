# https://leetcode.com/problems/island-perimeter/
# 463
def islandPerimeter(grid):
    for x in grid:
        x.append(0)
        x.insert(0, 0)
    grid.append([0 for _ in range(len(grid[0]))])
    grid.insert(0, [0 for _ in range(len(grid[0]))])
    res = 0
    for y in range(1,len(grid)-1):
        for x in range(1,len(grid[0])-1):
            if grid[y][x]:
                res += 4 - grid[y-1][x] - grid[y+1][x] - grid[y][x-1] - grid[y][x+1]
    return res


print(islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
