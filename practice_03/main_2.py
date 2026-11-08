def announce(func):
    def wrapper():
        result = func()
        print('Приветствую!')
        return result
    return wrapper

@announce
def hello():
    print('Привет!')
hello()
