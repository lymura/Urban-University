#Изменяемые и неизменяемые объекты. Кортежи

immutable_var = ([3, 4, 5], 8) + ('string', 'b') * 3
print(immutable_var)
immutable_var[0][1] = 9
print(immutable_var)

mutable_list = (1, 6, 'mut', 'list')
print(mutable_list)
mutable_list = (1, 6, 'mut', 'list') + (3, 4, 2) * 2
print(mutable_list)
