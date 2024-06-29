#Рекурсивное умножение цифр"

def get_multiplied_digits(number):
    str_number = str(number)

    # Удаляем ведущие нули, проверяя каждый символ
    while str_number and str_number[0] == '0':
        str_number = str_number[1:]

    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
       return int(str_number)

result = get_multiplied_digits(40203)
print(result)
