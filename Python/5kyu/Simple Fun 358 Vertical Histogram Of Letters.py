#
import re

def vertical_histogram_of(s):
    # your code here
    mat = re.findall(r'[A-Z ]+',s)
    a = sorted(''.join(mat).replace(' ',''))
    se = sorted(set(a))
    res = ' '.join(se)
    while a:
        buf = ''
        for x in se:
            if x in a:
                buf += '* '
                a.remove(x)
            else:
                buf += '  '
        res = buf[:-1].rstrip()+'\n' + res
    return res

print(vertical_histogram_of("AAABBC"))