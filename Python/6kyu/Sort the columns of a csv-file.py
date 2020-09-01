# https://www.codewars.com/kata/57f7f71a7b992e699400013f/train/python
def sort_csv_columns(csv_file_content):
    arr = csv_file_content.split('\n')
    t = []
    csv_columns = zip(*(row.split(';') for row in csv_file_content.split('\n')))
    print(list(csv_columns))
    for x in arr:
        t.append(list(enumerate(x.split(';'))))

    a = []
    for i in range(len(t[0])):
        b = []
        for n in range(len(t)):
            b.append(t[n][i])
        a.append(b)

    a = sorted(a, key=lambda x: x[0][1].lower())
    c = []
    for i in range(len(a[0])):
        b = []
        for n in range(len(a)):
            b.append(a[n][i][1])
        c.append(b)
    s = ''
    for x in c:
        s += ';'.join(x)+'\n'

    return s[:-1]


print(sort_csv_columns('myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n\
17945;10091;10088;3907;10132\n\
2;12;13;48;11'))