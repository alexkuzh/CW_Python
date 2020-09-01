# https://www.codewars.com/kata/593c0ebf8b90525a62000221/train/python
def group_groceries(groceries):
    category = {'fruit':[],'meat':[],'other':[],'vegetable':[]}
    for x in groceries.split(','):
        s = x.split('_')
        if s[0] in  category:
            category[s[0]].append(s[1])
        else:
            category['other'].append(s[1])
    s = ''
    for x in category:
        s += x+':'+','.join(sorted(category[x]))+'\n'
    return s.strip()


print(group_groceries('fruit_banana,vegetable_carrot,fruit_apple,canned_sardines,drink_juice,fruit_orange'))
