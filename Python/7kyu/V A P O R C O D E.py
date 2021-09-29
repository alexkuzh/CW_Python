# https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python
def vaporcode(s):
    #your code here
    return ' '.join(list(s.upper().replace(' ','')))


print(vaporcode('ass sdd fdf'))