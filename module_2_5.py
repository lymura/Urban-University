#Задача "Матрица воплоти":

def get_matrix(n, m, value):
    matrix = []                 #Создайте пустой список матрицы
    for i in range(n):          #первый цикл for для n строк матрицы
        row = []                #Создайте пустой список строк
        for j in range(m):       #второй цикл for для  m столбцов матрицы
            row.append(value)    #пополняйте пустой список значениями value
        matrix.append(row)
    return matrix                  #верните значение переменной matrix
    
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)



