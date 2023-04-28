# https://www.codewars.com/kata/63d1bac72de941033dbf87ae/train/python
def is_valid_sudoku(board):
    # проверка строк
    for row in board:
        if not is_valid_set(row):
            return False

    # проверка столбцов
    for col in range(9):
        column = [board[i][col] for i in range(9)]
        if not is_valid_set(column):
            return False

    # проверка квадратов 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_set(square):
                return False

    return True

def is_valid_set(nums):
    return sum(nums)==9