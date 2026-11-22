x =24
def show():
    x =14
    print(x)
show()
print(x)
#  х = 14 используется внутри функции и выводится в терминал при вызове функции, х = 24 является глобальной переменной и выводится при вызове принта

def total(*args):
    x = sum(args)
    print(x)
total(14,15,16)

def person(**kwargs):
    name = kwargs.get('name', 'Гость')
    age = kwargs.get('age', 0)
    return name, age
print(person(name ='Денис', age =20))

def increase(x):
    return x + 4
def apply(func, value):
    res = func(value)
    return(res)
print(apply(increase,3))

def countdown(n):
    if n == 0:
        return n
    else:
        print(n)
        return countdown(n-1)
countdown(3)
