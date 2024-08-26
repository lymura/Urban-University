def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Оба аргумента числа
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        # Оба аргумента строки
        return a + b
    else:
        # Аргументы разных типов или один из них не соответствует типам int, float, str
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # '123.456строка'
print(add_everything_up('яблоко', 4215))     # 'яблоко4215'
print(add_everything_up(123.456, 7))         # 130.456
