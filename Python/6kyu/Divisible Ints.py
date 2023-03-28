# https://www.codewars.com/kata/566859a83557837d9700001a/train/python
from collections import deque
from itertools import islice


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def get_count(n):
    s = str(n)
    r = 0
    for i in range(1,len(s)):
        for k in list(sliding_window(s, i)):
            num = int(''.join(k))
            try:
                if n % num == 0:
                    r+=1
            except:
                continue
    return r