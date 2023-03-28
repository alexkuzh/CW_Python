# https://www.codewars.com/kata/609eee71109f860006c377d1/train/python
def last_survivor(letters, coords):
    for n in coords:
        letters = letters[:n] + letters[n+1:]
    return letters



print(last_survivor('abc', [1, 1]))