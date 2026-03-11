def add(first_number, second_number):
    """Складывает два числа и возвращает результат."""
    return first_number + second_number

def sub(first_number, second_number):
    """Вычитает второе число из первого и возвращает результат."""
    return first_number - second_number

def mul(first_number, second_number):
    """Умножает два числа и возвращает результат."""
    return first_number * second_number

def div(first_number, second_number):
    """Делит первое число на второе и возвращает результат."""
    return first_number / second_number

if __name__ == "__main__":
    first_input = input('Введите первое число: ')
    second_input = input('Введите второе число: ')
    
    # Проверяем через IF: состоят ли введенные строки только из цифр?
    if not first_input.isdigit() or not second_input.isdigit():
        print("Ошибка: Пожалуйста, вводите только числа, а не буквы!")
    else:
        first_number = int(first_input)
        second_number = int(second_input)
        
        print(f"Результат сложения ({first_number} + {second_number}) = {add(first_number, second_number)}")
        print(f"Результат вычитания ({first_number} - {second_number}) = {sub(first_number, second_number)}")
        print(f"Результат умножения ({first_number} * {second_number}) = {mul(first_number, second_number)}")
        
        # Проверяем, не равен ли делитель нулю
        if second_number == 0:
            print("Ошибка: на 0 делить нельзя!")
        else:
            print(f"Результат деления ({first_number} / {second_number}) = {div(first_number, second_number)}")