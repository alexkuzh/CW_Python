# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
def subtractProductAndSum(n: int):
    a = list(str(n))
    return eval('*'.join(a)) - eval('+'.join(a))

print(subtractProductAndSum(234))