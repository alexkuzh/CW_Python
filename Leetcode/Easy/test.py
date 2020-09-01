def dec(func):
    def wrapper():
        print("Code before function")
        func()
        print("Code after function")
    return wrapper

def dec2(func):
    def wrapper():
        func()
        print('This is one more line')
    return wrapper

@dec2
@dec
def hello():
    print('Middle code')

hello()