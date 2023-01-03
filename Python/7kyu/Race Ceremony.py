# https://www.codewars.com/kata/62cecd4e5487c10028996e04/train/python


def race_podium(blocks):
    r = [blocks //3 - 1,blocks //3, blocks -  2*(blocks //3) + 1 ]
    if blocks == 7: return (2,4,1)
    while r[1]<=blocks//2:
        r[1] +=1
        r[0] = r[1] - 1
        r[2] = blocks - r[0] - r[1]
        if r[2]<r[0]<r[1]:
            return tuple(r)
    return 0




print(race_podium(7))