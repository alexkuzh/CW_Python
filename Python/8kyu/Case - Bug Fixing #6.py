# https://www.codewars.com/kata/55c933c115a8c426ac000082/train/python
def eval_object(v):
    # {'a':1,'b':1,'operation':'+'}
    return eval(str(v['a']) + v.get('operation') + str(v['b']))

print(eval_object({'a':1,'b':1,'operation':'+'}))