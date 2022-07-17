# https://www.codewars.com/kata/5b5fe164b88263ad3d00250b/train/python
def alphametics(puzzle):
    # your code goes here. you can do it!
    def remove_num(ch, n):
        md[ch] = n
        d.pop(ch)
        for x1 in d:
            d[x1].remove(n)

    d = {}
    md = {}
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in set(puzzle.replace(' + ', '').replace(' = ', '')):
        d[x] = num[:]
    summ = puzzle.split(' = ')[0].split(' + ')
    summ.append(puzzle.split(' = ')[1])

    print('*****',summ)
    for x in summ:
        if x[0] in d:
            if 0 in d[x[0]]:
                d[x[0]].remove(0)

    if len(summ[-1]) > max([len(x) for x in summ[:-1]]):
        remove_num(summ[-1][0],1)

    for d1 in md:
        puzzle = puzzle.replace(d1, str(md[d1]))

    d_copy = d.copy()
    # for d1 in d:

    # 97N4 +
    # 10R7
    #10871

    # print(md)

    return (f'{d}\n{md}\n{puzzle}')


print(alphametics('SEND + MORE = MONEY'))
