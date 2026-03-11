def add(first_number, second_number):
    """Складывает два числа и возвращает результат."""
    return first_number + second_number

def sub(first_number, second_number):
    """Вычитает второе число из первого и возвращает результат."""
    return first_number - second_number

def mul(first_number, second_number):
    """Умножает два числа и возвращает результат."""
    return first_number * second_number

if __name__ == "__main__":
    # Запрашиваем данные у пользователя (преобразуем введенную строку в целое число)
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    
    # Поочередно вызываем функции и выводим результаты в консоль
    print('Ответ:', add(first_number, second_number))
    print('Ответ:', sub(first_number, second_number))
    print('Ответ:', mul(first_number, second_number))