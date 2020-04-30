def correct_polish_letters(st):
    # your code here:
    d = {'ą':'a','ć':'c','ę':'e','ł':'l','ń':'n','ó':'o','ś':'s','ź':'z','ż':'z'}
    s = ''
    for x in st:
        s += d[x] if x in d else x
    return s

print(correct_polish_letters("Jędrzej Błądziński"))