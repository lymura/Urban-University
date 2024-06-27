# Глобальная переменная для подсчета вызовов функций
calls = 0

def count_calls(func):
    """Декоратор для подсчета вызовов функций."""
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper

#count_calls
def string_info(string):
    """Возвращает кортеж с информацией о строке."""
    return (len(string), string.upper(), string.lower())

#count_calls
def is_contains(string, list_to_search):
    """Проверяет, содержится ли строка в списке, не учитывая регистр."""
    return string.lower() in map(str.lower, list_to_search)

# Пример вызова функций
info = string_info("Hello World")
contains = is_contains("UrbaN", ["urban", "city", "town"])

# Вывод информации
print(info)  # Вывод: (11, 'HELLO WORLD', 'hello world')
print(contains)  # Вывод: True
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
print(f"Количество вызовов функций: {calls}")  # Вывод: Количество вызовов функций: