#Условная конструкция. Операторы if, elif, else

num_1 = input('Введите целое число:')
num_2 = input('Введите целое число:')
num_3 = input('Введите целое число:')
first = num_1
second = num_2
third = num_3

if first == second and second == third:      # Если все числа равны между собой, то вывести 3
    print(3)
elif first == second or second == third:        # Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
    print(2)
else:
    print(0)                                 # Если равных чисел среди 3-х вообще нет, то вывести 0