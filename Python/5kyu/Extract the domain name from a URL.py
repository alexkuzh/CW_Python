# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
import re

def domain_name(url):
    regex = r'[a-z0-9\-]+'
    url = url.replace('https://','').replace('http://','').replace('www.','')
    s = re.findall(regex,url)
    return s[0]

print(domain_name('https://youtube.com'))