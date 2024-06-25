#Распаковка позиционных параметров"

def print_params(a = 1, b = 'строка', c = True):
    print(f"a: {a}, b: {b}, c: {c}")

    # Вызов функции без аргументов
print_params()

# Вызов функции с одним аргументом
print_params(10)

# Вызов функции с двумя аргументами
print_params(10, 'новая строка')

# Вызов функции с тремя аргументами
print_params(10, 'новая строка', False)

# Вызов функции с именованными аргументами
print_params(b=25)
print_params(c=[1, 2, 3])

#2.Распаковка параметров:

values_list = [2, 'str', True]
values_dict = {'a': 3.14, 'b': 'словарь', 'c': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
