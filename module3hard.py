#Дополнительное практическое задание по модулю: "Подробнее о функциях."
def calculate_structure_sum(data_structure):

    sum = 0
    # проверка data_structure  является  list, tuple или set?
    if isinstance(data_structure, (list, tuple, set)):
        for element in data_structure:
            # рекурсивный вызов функции для каждого элемента
            sum += calculate_structure_sum(element)

    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():

            sum += len(key)
            # рекурсивный вызов функции для  value
            sum += calculate_structure_sum(value)
    # проверка data_structure - str?
    elif isinstance(data_structure, str):
        # Add the length of the string to the sum
        sum += len(data_structure)
    # проверка data_structure - (int или  float)?
    elif isinstance(data_structure, (int, float)):
        sum += data_structure
    return sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)