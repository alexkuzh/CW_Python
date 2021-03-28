# https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python
def sumofsquare(n):
    C = [[0 for i in range(n + 1)]
         for j in range(n + 1)]

    # Calculate value of
    # Binomial Coefficient
    # in bottom up manner
    for i in range(0, n + 1):

        for j in range(0, min(i, n) + 1):

            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1

            # Calculate value
            # using previously
            # stored values
            else:
                C[i][j] = (C[i - 1][j - 1] +
                           C[i - 1][j])

    sum = 0
    for i in range(0, n + 1):
        sum = sum + (C[n][i] *
                     C[n][i])

    return sum


n = 4
print(sumofsquare(n), end="\n")
