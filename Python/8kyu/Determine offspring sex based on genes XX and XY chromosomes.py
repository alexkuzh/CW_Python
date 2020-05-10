# https://www.codewars.com/kata/56530b444e831334c0000020/train/python
def chromosome_check(sperm):
    #Your code here
    return 'Congratulations! You\'re going to have a {}.'.format('son' if sperm[1]=='Y' else 'daughter')