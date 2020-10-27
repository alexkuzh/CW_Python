# df%&cf#gff*(s#
# sf%&fg#fcf*(d#

# def filter_string(original_str):
#     return ''.join(ch for ch in original_str if ch.isalpha())
#
# a = 'df%&cf#gff*(s#'
# b = filter_string(a)
# c = b[::-1]
# print(b)
# print(c)
# '''
# Одна и та же функция конвертирует туда и обратно
# Первый шаг: Убираем symbols из a >> string b
# 11:35
# Второй шаг: Разворачиваем string b >> string c = b[::-1]
# 11:37
# Третий шаг: Пробегаем по элементам первоначального string a, и
# (пропуская symbols) заменяем буквы на элементы c, получая string d
# '''
# def convert_string(original_str, inverted_substr):
#     converted_str = original_str
#     k = 0;
#     j = 0;
#     for i in original_str:
#         if i.isalpha():
#             # converted_str[j] = inverted_substr[k]
#             converted_str = converted_str[:j] + inverted_substr[k] + converted_str[j + 1:]
#             k = k+1;
#         j = j+1;
#     return converted_str
#
# d = convert_string(a,c)
# print(a)
# print(d)

def convert(st):
    chars = [x for x in st if x.isalpha()][::-1]
    sym = [x for x in st if not x.isalpha()]
    return ''.join([chars.pop(0) if m else sym.pop(0) for m in [x.isalpha() for x in st]])


def convert_wide(st):
    chars, sym, a, s = [], [], [], []
    for x in st:
        if x.isalpha():  # Усли это буква
            chars.append(x)
            a.append(True)
        else:
            sym.append(x)
            a.append(False)

    chars = chars[::-1]  # перевернули

    for m in a:
        if m:
            b = chars.pop(0)
            s.append(b)
        else:
            b = sym.pop(0)
            s.append(b)
        print(chars)
        print(sym)
        print(s)

    return ''.join(s)


print(convert_wide('sf%&fg#fcf*(d#'))
