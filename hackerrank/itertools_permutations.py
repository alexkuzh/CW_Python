# https://www.hackerrank.com/challenges/itertools-permutations/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def permute(S, soFar, k):
    if len(soFar) == k:
        print(soFar)
        return
    else:
        for i in range(len(S)):
            permute(S[:i] + S[i+1:], soFar + S[i], k)

if __name__ == '__main__':
    S, k = input().split()
    permute(sorted(S), "", int(k))