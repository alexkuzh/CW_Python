# https://leetcode.com/problems/shuffle-string/
def restoreString(s, indices):
    return ''.join([x[0] for x in sorted(list(zip(list(s),indices)),key=lambda x: x[1])])

print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
