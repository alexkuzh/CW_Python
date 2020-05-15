# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
def series_sum(n):
# Happy Coding ^_^
    a = 0
    for i in range(0,n):
        a += 1/(i*3+1)
    return '%.2f' % a

print(series_sum(1))