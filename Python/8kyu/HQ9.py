def HQ9(code):
    if code == 'H': return 'Hello World!'
    elif code == 'Q': return 'Q'
    elif code == '9':
        s = ''
        for i in range(99, 2, -1):
            s += str(i) + ' bottles of beer on the wall, '+str(i)+' bottles of beer.\n' \
                'Take one down and pass it around, ' + str(i-1)+' bottles of beer on the wall.\n'
        s = s + '2 bottles of beer on the wall, 2 bottles of beer.\n' \
                'Take one down and pass it around, 1 bottle of beer on the wall.\n' +\
                '1 bottle of beer on the wall, 1 bottle of beer.\n' \
                'Take one down and pass it around, no more bottles of beer on the wall.\n' \
                'No more bottles of beer on the wall, no more bottles of beer.\n' \
                'Go to the store and buy some more, 99 bottles of beer on the wall.'
        return s

print(HQ9('9'))
