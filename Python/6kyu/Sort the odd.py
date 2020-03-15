# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
def sort_array(s):
    # Return a sorted array.
    if s == []: return []
    oddA = []
    evenA = []
    A = []
    for i in range(0,len(s)):
        if s[i] % 2 == 1 and s[i] != 0:
            oddA.append(s[i])
            A.append(False)
        else:
            evenA.append(s[i])
            A.append(True)
    oddA.sort()
    m = []
    for x in A:
        m.append(evenA.pop(0)) if x else m.append(oddA.pop(0))
    return m