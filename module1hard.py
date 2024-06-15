# Задание "Средний балл"

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = sorted(students)
print(students_)

a = students_[0]
print(a)
grade = grades[0]
print(grade)
average = sum(grade) / len(grade)
print(average)

peoples = {a:  average}
print(peoples)

b = students_[1]
print(b)
grade = grades[1]
print(grade)
average = sum(grade) / len(grade)
print(average)

peoples.update({b:  average})
print(peoples)

c = students_[2]
print(c)
grade = grades[2]
print(grade)
average = sum(grade) / len(grade)
print(average)

peoples.update({c:  average})
print(peoples)

d = students_[3]
print(d)
grade = grades[3]
print(grade)
average = sum(grade) / len(grade)
print(average)

peoples.update({d:  average})
print(peoples)

i = students_[4]
print(i)
grade = grades[4]
print(grade)
average = sum(grade) / len(grade)
print(average)

peoples.update({i:  average})
print(peoples)