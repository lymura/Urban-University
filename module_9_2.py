first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список длин строк из first_strings, длина которых не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Список пар слов одинаковой длины из first_strings и second_strings
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Словарь строк с четной длиной из объединенных списков
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Примеры вывода
print(first_result)
print(second_result)
print(third_result)
