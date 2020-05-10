# https://www.codewars.com/kata/57126304cdbf63c6770012bd/train/python
def isDigit(string):
#11ELF
    try:
        float(string)
        return True
    except:
        return False

print(isDigit('33'))