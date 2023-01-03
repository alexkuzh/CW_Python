# https://www.codewars.com/kata/6262f9f7afc4729d8f5bef48/train/python

def white_black_areas(cs, rs):

    od_cs = sum([n for i,n in enumerate(cs) if i%2])
    ev_cs = sum([n for i,n in enumerate(cs) if not i%2])
    od_rs = sum([n for i,n in enumerate(rs) if i%2])
    ev_rs = sum([n for i,n in enumerate(rs) if not i%2])
    white = od_rs*od_cs + ev_rs*ev_cs
    return (white, sum(cs)*sum(rs)-white)


print(white_black_areas([3,1,2,7,1],[1,8,4,5,2]))