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
    
    # Выводим результаты с понятными текстовыми пояснениями
    print(f"Результат сложения ({first_number} + {second_number}): {add(first_number, second_number)}")
    print(f"Результат вычитания ({first_number} - {second_number}): {sub(first_number, second_number)}")
    print(f"Результат умножения ({first_number} * {second_number}): {mul(first_number, second_number)}")