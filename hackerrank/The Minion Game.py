# https://www.hackerrank.com/challenges/the-minion-game/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def minion_game(s):
    # your code goes here
    vov = ('A', 'E', 'I', 'O', 'U')
    st, ke = 0, 0
    for i in range(len(s)):
        if s[i] in vov:
            ke += len(s) - i
        else:
            st += len(s) - i
    if st == ke:
        print('Draw')
    else:
        print(f'Stuart {st}' if st > ke else f'Kevin {ke}')


if __name__ == '__main__':
    s = input()
    minion_game(s)
