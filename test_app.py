from app import add, sub, mul, div  # Добавили импорт div

def test_add_multiply_divide():
    assert add(6, 3) == 9
    assert sub(6, 3) == 3
    assert mul(6, 3) == 18
    assert div(6, 3) == 2.0  # Добавили проверку деления (результат в Python всегда float)

def test_divide_by_one():
    assert add(7, 1) == 8
    assert sub(7, 1) == 6
    assert mul(7, 1) == 7
    assert div(7, 1) == 7.0  # Добавили проверку деления

def test_zero():
    assert add(0, 5) == 5
    assert sub(0, 5) == -5
    assert mul(0, 5) == 0
    assert div(0, 5) == 0.0  # Добавили проверку деления (0 делить на 5 можно)