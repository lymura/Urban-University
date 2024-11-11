first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин строк, если их длины не равны
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))

# Генераторная сборка для сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
second_result = (len(first[i]) > len(second[i]) for i in range(min(len(first), len(second)))

print(list(first_result))
print(list(second_result))
