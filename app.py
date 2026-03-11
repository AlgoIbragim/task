def add(first_number, second_number):
    return first_number + second_number

def sub(first_number, second_number):
    return first_number - second_number

def mul(first_number, second_number):
    return first_number * second_number

if __name__ == "__main__":
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    
    print('Ответ:', add(first_number, second_number))
    print('Ответ:', sub(first_number, second_number))
    print('Ответ:', mul(first_number, second_number))