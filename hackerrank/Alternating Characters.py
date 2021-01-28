# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def alternatingCharacters(s):
    # if s.count('A') == 0 or s.count('B') == 0:
    #     return len(s) - 1
    # return len(s) - 2*max(s.count('AB'), s.count('BA'))
    count = 0
    for num in range (len(s)-1):
        if s[num] == s[num+1]:
            count +=1
    return count

print(alternatingCharacters('ABABABAA'))
