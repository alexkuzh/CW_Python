# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
def likes(names):
    if not names: return 'no one likes this'
    if len(names) == 1: return '{} likes this'.format(names[0])
    if len(names) == 2: return  '{} and {} like this'.format(names[0],names[1])
    if len(names) == 3: return  '{}, {} and {} like this'.format(names[0],names[1],names[2])
    if len(names) >= 4: return  '{}, {} and {} others like this'.format(names[0],names[1],str(len(names)-2)

print(likes(['aaa','bbb']))

    #
    # n = len(names)
    # return {
    #     0: 'no one likes this',
    #     1: '{} likes this',
    #     2: '{} and {} like this',
    #     3: '{}, {} and {} like this',
    #     4: '{}, {} and {others} others like this'
    # }[min(4, n)].format(*names[:3], others=n-2)