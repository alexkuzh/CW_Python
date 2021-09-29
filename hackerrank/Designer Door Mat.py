# n,m =9,27
s = input().split()
n,m = int(s[0]),int(s[1])
# print(s)
for x in range(n//2):
    print('-'*(m//2-x*3-1)+'.|.'+'.|.'*(x*2) + '-'*(m//2-x*3-1))
print('-'*(n)+'WELCOME'+'-'*(n))
for x in range(n//2-1,-1,-1):
    print('-'*(m//2-x*3-1)+'.|.'+'.|.'*(x*2) + '-'*(m//2-x*3-1))