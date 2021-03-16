# def order_weight(_str):
#     return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
#

# def sum_string(s):
#     sum = 0
#     for digit in s:
#         sum += int(digit)
#     return sum
#
# def order_weight(strng):
#     # your code
#     initial_list = sorted(strng.split())
#     result = " ".join(sorted(initial_list, key=lambda x: sum(int(c) for c in x)))
#     return result

#
# print(order_weight("103 123 4444 99 2000"))


# def cakes(recipe, available):
#     m = 10000
#     for x in recipe.keys():
#         if available.get(x) == None: return 0
#         if available.get(x) // recipe.get(x) < m:
#             m = available.get(x) // recipe.get(x)
#     return m

# def cakes(recipe, available):
#     return min([available[i]//recipe[i] if i in available else 0 for i in recipe])

#
# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# print(cakes(recipe,available))

# def zeros(n):
#     a = 0
#     for i in range(1,13):
#         a += n//(5**i)
#     return a

# def zeros(n):
#     x = n/5
#     return x+zeros(x) if x else 0

# def zeros(n):
#     result = 0
#     while n != 0:
#         result += n / 5
#         n = n / 5
#     return result

# def first_non_repeating_letter(string):
#     string_lower = string.lower()
#     for i, letter in enumerate(string_lower):
#         if string_lower.count(letter) == 1:
#             return string[i]
#     return ""

# def first_non_repeating_letter(string):
#     singles = [i for i in string if string.lower().count(i.lower()) == 1]
#     print(singles)
#     return singles[0] if singles else ''
#
# print(first_non_repeating_letter('stress'))

# def scramble(s1, s2):
#     # your code here
#     d1 = {}
#     d2 = {}
#     for x in set(s1):
#         d1[x]=s1.count(x)
#     print(d1)
#     for x in set(s2):
#         d2[x]=s2.count(x)
#     print(d2)
#     for x in d2:
#         try:
#             if d2[x]>d1[x]: return False
#         except:
#             return False
#     return True
#
#
# def scramble(s1, s2):
#     # your code here
#     s = list(s1)
#     for x in s2:
#         if x in s1:
#             try:
#                 s.remove(x)
#             except:
#                 return False
#         else:
#             return False
#     return True

# def scramble(s1,s2):
#     for c in set(s2):
#         if s1.count(c) < s2.count(c):
#             return False
#     return True
#
# print(scramble('rrrkqoodlww', 'wworld'))

# def generate_hashtag(s):
#     #your code here
#     if len(s) ==0 or len(s) > 140 : return False
#     return '#'+s.title().replace(' ','')

# def generate_hashtag(s):
#     if not s or len(s)>140:
#         return False
#     return "#"+''.join(x.capitalize() for x in s.split(' '))
#
# print(generate_hashtag(" Hello there thanks for trying my Kata"))

# import re
#
# def domain_name(url):
#     regex = r'[a-z0-9\-]+'
#     url = url.replace('https://','').replace('http://','').replace('www.','')
#     s = re.findall(regex,url)
#     print(s)
#     return s[0]

# def domain_name(url):
#     url = url.replace('www.','')
#     url = url.replace('https://','')
#     url = url.replace('http://','')
#     return url[0:url.find('.')]
#
# print(domain_name("http://github.com/carbonfive/raygun"))

# def score(dice):
#     obj = [['111',1000], ['666',600], ['555', 500], ['444',400], ['333',300], ['222',200], ['1',100], ['5',50]]
#     s = ''.join(str(x) for x in (sorted(dice)))
#     print(s)
#     a = 0
#     for i in range(0, 5):
#         for j in range(0, 8):
#             if s.find(obj[j][0]) >= 0:
#                 a += obj[j][1]
#                 s = s.replace(obj[j][0], '', 1)
#                 print(s)
#     return a
# def score(dice):
#     sum = 0
#     counter = [0,0,0,0,0,0]
#     points = [1000, 200, 300, 400, 500, 600]
#     extra = [100,0,0,0,50,0]
#     for die in dice:
#         counter[die-1] += 1
#
#     for (i, count) in enumerate(counter):
#         sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)
#
#     return sum

# def score(dice):
#     sum, c1, c5 = 0, dice.count(1), dice.count(5)
#     if c1 >= 3:
#         c1 -= 3
#         sum += 1000
#     sum += 100 * c1
#
#     if c5 >= 3:
#         c5 -= 3
#         sum += 500
#     sum += 50 * c5
#
#     if dice.count(6) >= 3: sum += 600
#     if dice.count(4) >= 3: sum += 400
#     if dice.count(3) >= 3: sum += 300
#     if dice.count(2) >= 3: sum += 200
#     return sum


# print(score([2, 4, 4, 5, 4]))

# def fibo(n):
#     a, b, c = 1, 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#         c += a
#         return c
#
#
# def perimeter(n):
#     # your code
#     return 4 * fibo(n + 1)

# def perimeter(n):
#     a, b = 1, 2
#     while n:
#         a, b, n = b, a + b, n - 1
#     return 4 * (b - 1)

# def increment_string(s):
#     a = ''
#     for i in range(len(s)-1, -1, -1):
#         if s[i].isdigit():
#             m = i
#             a = s[i] + a
#         else:
#             break
#     # print(s)
#     print(m)
#     print(a)
#     if a == '':
#         return s + '1'
#     else:
#         print(str(int(a)+1).zfill(len(a)))
#         return s[0:m] + str(int(a)+1).zfill(len(a))
#
# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))
#
# def increment_string(s):
#     if s and s[-1].isdigit():
#         return increment_string(s[:-1]) + "0" if s[-1] == "9" else s[:-1]
#     return s + "1"
# import re
#
# def increment_string(input):
#     match = re.search("(\d*)$", input)
#     if match:
#         number = match.group(0)
#         if number.isdigit():
#             return input[:-len(number)] + str(int(number) + 1).zfill(len(number))
#     return input + "1"


# print(increment_string('foobar001'))

a = [1, 3]
b = [3]
print(list(filter(lambda x: x > b[-1], a))[0])