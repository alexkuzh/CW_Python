# https://www.codewars.com/kata/62a3855fcaec090025ed2a9a/train/python
import collections

days = [(['7.4.9', '8'], ['Infantry charge', 'Medical helicopters spotted']),
        (['3.8', '7.4.9'], ['Infantry charge', 'Pizza delivery spotted']),
        (['7.6'], ['Infantry charge'])]

days = [(['8', '4.4.4', '2', '6', '1.7', '2.7.9'], ['Orange army retreats', 'Medical helicopters spotted', 'Ceasefire called',
                                                    'Ceasefire called', 'Orange army charges', 'Orange army charges']),
        (['9.9.6', '4.4.4', '6', '5.1.6', '2', '9'], ['Orange army charges', 'Infantry spotted', 'Orange army charges',
                                                      'Infantry spotted', 'Ceasefire called', 'Missile launchers spotted']),
        (['8', '6.1.5', '1.7', '6', '4.4.4'], ['Missile launchers spotted', 'Orange army retreats', 'Orange army charges',
                                               'Medical helicopters spotted', 'Ceasefire called']),
        (['4.6.9', '4.4.4', '6', '9'], ['Orange army charges', 'Infantry spotted', 'Ceasefire called', 'Missile launchers spotted']),
        (['2', '9.9.6', '6.1.5', '9'], ['Infantry spotted', 'Missile launchers spotted', 'Infantry spotted', 'Orange army charges']),
        (['2', '4.6.9', '1.7', '4.4.4'], ['Missile launchers spotted', 'Orange army charges',
                                          'Medical helicopters spotted', 'Ceasefire called'])]

days = [(['8.8.6', '2.2.4', '9'], ['Ambush in the jungle', 'Ambush in the jungle', 'Ambush in the jungle']),
        (['4', '5'], ['General assassinated', 'Tanks charge']),
        (['2', '8.8.6', '4'], ['Orange army charges', 'Ambush in the jungle', 'Tanks charge']),
        (['9', '2', '2.2.4'], ['Ambush in the jungle', 'Orange army charges', 'Ambush in the jungle'])]


days = [(['5.2.8', '8'], ['Tanks spotted', 'Attack helicopters spotted']),
        (['5.2.8', '8.9', '7.7.9', '4.1.9', '5.8'], ['Tanks spotted', 'Ambush in the jungle', 'Ceasefire called', 'Attack helicopters spotted', 'Infantry charge']),
        (['5.8', '8', '1.1.1', '4.1.9', '5.2.8'], ['Attack helicopters spotted', 'Ceasefire called', 'Tanks spotted', 'Camp golf attacked', 'Tanks spotted']),
        (['8.9', '4.1.9', '8'], ['Ceasefire called', 'Ambush in the jungle', 'Tanks spotted'])]

'''
{'5.2.8': 'Attack helicopters spotted', 
'8.9': 'Ambush in the jungle', 
'7.7.9': 'Infantry charge', 
'8': 'Tanks spotted', 
'4.1.9': 'Ceasefire called', 
'5.8': 'Tanks spotted'} should equal {'1.1.1': 'Camp golf attacked', 
'7.7.9': 'Infantry charge', 
'8': 'Tanks spotted', 
'5.8': 'Tanks spotted', 
'5.2.8': 'Attack helicopters spotted', 
'8.9': 'Ambush in the jungle', 
'4.1.9': 'Ceasefire called'}
'''

# a = sorted(days, key=lambda x: len(x[0]))
# print(a)

d = {}

days.sort(key=lambda x: len(x[0]))
for x in days:
        print(x)

print('===============================================')

def delete_(num, st):
        for message in days:
                if num in message[0]:
                        message[0].remove(num)
                        # if st in message[1]:
                        message[1].remove(st)

# while days:
for _ in range(len(days)):
        #clear one
        for message in days:
                if len(message[0]) == 1:
                        d[message[0][0]] = message[1][0]
                        days.remove(message)
                        delete_(message[0][0],message[1][0])
                if len(set(message[1])) == 1:
                        for x in message[0]:
                                d[x] = message[1][0]
                                delete_(x, message[1][0])

        for i in range(len(days)):
                for k in range(i+1, len(days)):
                        a1 = set(days[i][0])
                        a2 = set(days[k][0])
                        n1 = set(days[i][1])
                        n2 = set(days[k][1])
                        ra = a1.difference(a2)
                        na = n1.difference(n2)
                        ra1 = a1.intersection(a2)
                        na1 = n1.intersection(n2)
                        if len(ra) == 1 and len(na) == 1:
                                ra_v = ra.pop()
                                na_v = na.pop()
                                d[ra_v] = na_v
                                delete_(ra_v, na_v)
                        elif len(ra1) == 1 and len(na1) == 1:
                                ra_v = ra1.pop()
                                na_v = na1.pop()
                                d[ra_v] = na_v
                                delete_(ra_v, na_v)

# print(days)
print(d)

#
# d1 = set(['8.8.6', '2.2.4', '9'])
# d2 = set(['2', '8.8.6', '4'])
# d3 = set(['4', '5'])
# d4 = set(['2', '8.8.6', '4'])
# print(d1.intersection(d2))
# print(d3.difference(d4))

