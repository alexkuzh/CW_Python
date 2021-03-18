# https://www.hackerrank.com/test/5qqdbqh3j95/questions/3pramr7a684
def oddNumbers(l, r):
    # Write your code here

    return [x for x in range(l if l%2 else l+1,r+1,2)]


print(oddNumbers(2,5))