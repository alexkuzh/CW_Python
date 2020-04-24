# https://www.codewars.com/kata/52fba66badcd10859f00097e/python
def disemvowel(st):
    s = ['i','e','o','a','I','E','A','O','u','U']
    for x in s:
        st = st.replace(x,'')
    return st


print(disemvowel("This website is for losers LOL!"))