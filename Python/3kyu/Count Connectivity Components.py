# https://www.codewars.com/kata/5856f3ecf37aec45e6000091
from collections import deque, Counter


def fill(grid, x, y):
    h, w = len(grid), len(grid[x])
    unexplored = deque([(x, y)])
    size = 0
    while unexplored:
        x, y = unexplored.popleft()
        if 0 <= x < h and 0 <= y < w and grid[x][y] == ' ':
            grid[x][y] = '#'
            unexplored.extend(((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)))
            size += x % 2 == 1 and y % 3 == 1
    return size


def components(diagram):
    grid = [list(line) for line in diagram.split('\n')]
    cells = ((x, y) for x in range(len(grid)) for y in range(len(grid[x])))
    sizes = Counter(fill(grid, x, y) for x, y in cells if grid[x][y] == ' ')
    return sorted(sizes.items(), reverse=True)
