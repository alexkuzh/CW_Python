class Solution:
    def fizzBuzz(n):
        a = []
        for i in range(1,n+1):
            c = ''
            if i % 3 == 0:
                c += 'Fizz'
            if i % 5 == 0:
                c += 'Buzz'
            if c == '':
                a.append(i)
            else:
                a.append(c)
        return a


print(Solution.fizzBuzz(15))