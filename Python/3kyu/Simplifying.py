# https://www.codewars.com/kata/57f2b753e3b78621da0020e8/train/python
'''
не доделал, плюнул 2021/02/16
'''
def simplify(ex, fo):
    f = ''
    for x in ex:
        d = {}
        for m in str(x).replace('\'','').replace(']','').replace('[','').split(', '):
            # print(m)
            d[m.split(' = ')[1]]=m.split(' = ')[0]
        print(d)
        for x in fo:
            for s in x.split('+')




    return formula[0]

examples=[["a + a = b", "b - d = c", "a + b = d"],
          ["a + 3g = k", "-70a = g"],
          ["-j -j -j + j = b"]
          ]
formula=["c + a + b",
         "-k + a",
         "-j - b"
         ]
print(simplify(examples,formula))
