def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        i = 99
        s = ''
        while i > 1:
            s = s + str(i) + ' bottles of beer on the wall, ' + str(i) + ' bottles of beer.\nTake one down and pass it around, '+ str(i-1) + ' bottles of beer on the wall.\n'
            i -=1
        s = s + '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        return s

print(HQ9('9'))