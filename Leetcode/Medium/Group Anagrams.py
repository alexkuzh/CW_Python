def groupAnagrams(strs):
    a = []
    while strs:
        d = []
        for i in range(1, len(strs)):
            w1 = sorted(strs[0])
            w2 = sorted(strs[i])
            if sorted(strs[0]) == sorted(strs[i]):
                d.append(strs[i])
        d.append(strs.pop(0))
        a.append(d)
        for x in d:
            if x in strs:
                strs.remove(x)
    return a


# print(comp('eat', 'tea'))
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams(["2","2","2"]))
print(groupAnagrams(["b"]))
print(groupAnagrams(["","b",""]))
