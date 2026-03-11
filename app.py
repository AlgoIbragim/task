def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

if __name__ == "__main__":
    a = int(input('первое число: '))
    b = int(input('второе число: '))
    print('Ответ:', add(a,b))
    print('Ответ:', sub(a,b))
    print('Ответ:', mul(a,b))