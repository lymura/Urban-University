#Задание "Слишком древний шифр"

import random
def generate_password():     # Генерируем случайное число от 3 до 20 для первого поля
    num = list(range(3, 20))
    first_field = random.choice(num)
    print(first_field)

    pairs = []
    numbers = list(range(1, 21))
    if first_field in numbers:
        numbers.remove(first_field)
        print(numbers)

    for i in numbers:
        for j in numbers:

            if (i + j) % first_field == 0 and j < first_field:
                pairs.append(f'{i}{j}')
    second_field = ''.join(pairs)
    return first_field, second_field
password = generate_password()

print(f'{password}')
