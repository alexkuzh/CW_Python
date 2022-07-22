#https://www.codewars.com/kata/5db8a241b8d7260011746407/train/python

def tetris(arr) -> int:
    a = {}
    print(arr)
    for x in arr:
        b = a.get(x[1:])
        if b is None:
            a[x[1:]] = int(x[0])
        else:
            a[x[1:]] = b + int(x[0])
        if (len(a.keys()) < 9) and (max(a.values()) > 30):
            return 0
        if max(a.values()) - min(a.values()) >= 30:
            return min(a.values())
    if len(a.keys())<9:
        return 0
    return min(a.values())


print(tetris(['1R3', '4R3', '3R2', '4R1', '4L3', '4L2', '3R1', '1L1', '4R1', '4R1',
              '4R1', '1L3', '3L1', '1R1', '2R1', '2R0', '4R1', '1L4', '4R3', '2R1',
              '4R1', '4R2', '3L2', '2R4', '3L2']))