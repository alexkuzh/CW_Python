# https://www.codewars.com/kata/57814d79a56c88e3e0000786
def decrypt(encrypted_text, n):
    if encrypted_text == None:
        return None
    else:
        s = list(encrypted_text)
        if n <= 0:
            return encrypted_text
        else:
            for i in range(0, n):
                l1 = s[:len(s) // 2]
                l2 = s[len(s) // 2:]
                l = []
                for n in range(0, len(l1)):
                    l.append(l2[n])
                    l.append(l1[n])
                if len(encrypted_text) % 2 == 1:
                    l.append(l2[n + 1])
                s = l
    return ''.join(l)


def encrypt(text, n):
    if text == None:
        return None
    else:
        s = list(text)
        if n <= 0:
            return text
        else:
            for i in range(0, n):
                l = s[1::2] + s[0::2]
                s = l
    return ''.join(l)