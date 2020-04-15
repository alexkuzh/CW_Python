class Calculator(object):

    def evaluate(self, string):
        a = string.split(' ')
        i = 0
        while i < len(a):
            if a[i] == '*':
                b = str(float(a[i - 1]) * float(a[i + 1]))
                a[i - 1] = b
                a.pop(i)
                a.pop(i)
                i = 0
            elif a[i] == '/':
                b = str(float(a[i - 1]) / float(a[i + 1]))
                a[i - 1] = b
                a.pop(i)
                a.pop(i)
                i = 0
            i += 1
        i = 0
        print(a)
        while i < len(a):
            if a[i] == '+':
                b = str(float(a[i - 1]) + float(a[i + 1]))
                a[i - 1] = b
                a.pop(i)
                a.pop(i)
                i = 0
            elif a[i] == '-':
                b = str(float(a[i - 1]) - float(a[i + 1]))
                a[i - 1] = b
                a.pop(i)
                a.pop(i)
                i = 0
            i += 1
        return float(a[0])


print(Calculator().evaluate('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'))
