first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин строк, если их длины не равны
first_result = (abs(len(first[i]) - len(second[i])) for i in range(min(len(first), len(second))) if len(first[i]) != len(second[i]))

# Генераторная сборка для сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

# Примеры вывода
print(list(first_result))
print(list(second_result))
