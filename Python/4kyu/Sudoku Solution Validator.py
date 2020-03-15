# https://www.codewars.com/kata/529bf0e9bdf7657179000008
def valid_solution(board):
    for i in range(0, 9):
        row = sum(set([x for x in board[i] if x >=1 and x <=9]))
        if row != 45: return False
        col = 0
        for n in range(0, 9):
            col += board[n][i]
        if col != 45: return False
        sq = board[i // 3 * 3]    [n // 3 * 3] + board[i // 3 * 3]    [n // 3 * 3 + 1] + board[i // 3 * 3]    [n // 3 * 3 + 2] + \
             board[i // 3 * 3 + 1][n // 3 * 3] + board[i // 3 * 3 + 1][n // 3 * 3 + 1] + board[i // 3 * 3 + 1][n // 3 * 3 + 2] + \
             board[i // 3 * 3 + 2][n // 3 * 3] + board[i // 3 * 3 + 2][n // 3 * 3 + 1] + board[i // 3 * 3 + 2][n // 3 * 3 + 2]
        if sq != 45: return False
    return True
