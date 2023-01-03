# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python

def up_array(arr):
    if min(arr)<0 or max(arr)>9: return None
    return list(map(int,list(str(int(''.join((map(str,arr))))+1).zfill(len(arr)))))

print(up_array([0,1,9]))

