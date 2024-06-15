#Словари и множества

my_dict = {'Mike': 2014, 'Nik': 2020, 'Pit': 2022, 'Leila': 2023}
print('my_dict:', my_dict)
print('Existing_value:', my_dict['Pit'])
print('Not existing value:', my_dict.get('Leo'))
print('Not existing value:', my_dict.get('Leo', 'не существующий ключ'))
my_dict.update({'Victor': 2012, 'Jon': 2004})     #Добавьте две произвольные пары в словарь
print(my_dict)
d = my_dict.pop('Victor')    #удалите одну из пар
print(d)      #выведите значение из этой пары на экран
print(my_dict)

#Работа с множествами
my_set = {1, 4, 4, 21, 1, 'f', 'f', True, 'vip', 65, 0, 0}
print(my_set)
my_set.add('e')      #Добавьте 2 произвольных элемента
my_set.add(2)
print(my_set)
my_set.remove('vip')         # Удалите один любой элемент
print(my_set)


