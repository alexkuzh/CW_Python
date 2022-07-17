# https://www.codewars.com/kata/5902bc7aba39542b4a00003d/train/python

z = ['antelope eats grass',
     'big-fish eats little-fish',
     'bug eats leaves',
     'bear eats big-fish',
     'bear eats bug',
     'bear eats chicken',
     'bear eats cow',
     'bear eats leaves',
     'bear eats sheep',
     'chicken eats bug',
     'cow eats grass',
     'fox eats chicken',
     'fox eats sheep',
     'giraffe eats leaves',
     'lion eats antelope',
     'lion eats cow',
     'panda eats leaves',
     'sheep eats grass']

d = [['antelope', 'grass'], ['big-fish', 'little-fish'], ['bug', 'leaves'], ['bear', 'big-fish'], ['bear', 'bug'],
     ['bear', 'chicken'], ['bear', 'cow'], ['bear', 'leaves'], ['bear', 'sheep'], ['chicken', 'bug'], ['cow', 'grass'],
     ['fox', 'chicken'], ['fox', 'sheep'], ['giraffe', 'leaves'], ['lion', 'antelope'], ['lion', 'cow'],
     ['panda', 'leaves'], ['sheep', 'grass']]


def who_eats_who(zoo):
    # Your code here
    a = []
    z = zoo.split(',')
    z.append(' ')
    z.insert(0, ' ')
    t = True
    while t:
        print(z)
        for i in range(1, len(z) - 1):
            if [z[i],z[i-1]] in d:
                a.append(f'{z[i]} eats {z[i - 1]}')
                z.pop(i - 1)
                break
            if [z[i],z[i+1]] in d:
                a.append(f'{z[i]} eats {z[i + 1]}')
                z.pop(i + 1)
                break
        else:
            t = False
    # a.insert(0,zoo)
    a.append(','.join(z).strip().strip(','))
    return a


if __name__ == '__main__':
    print(who_eats_who("leaves,grass,bug,bug,leaves,chicken,busker"))

'''
'bug eats leaves', 
'chicken eats bug', 
'chicken eats bug', 
'leaves,grass,chicken,busker'
'''