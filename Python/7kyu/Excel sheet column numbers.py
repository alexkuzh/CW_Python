# https://www.codewars.com/kata/55ee3ebff71e82a30000006a/train/python
def title_to_number(title):
    return sum([(ord(title[-i])-64) * 26**(i-1) for i in range(1,len(title)+1)])
