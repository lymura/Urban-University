## Задача "Многопроцессное считывание":
import multiprocessing
import threading
import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()  #чтение из файла построчно
            if not line:            #Проверяет, является ли строка пустой
                break
            all_data.append(line.strip())  #Добавляет строку c удаленными пробелами и символами

    return all_data                  #Возвращает список, содержащий все строки, считанные из файла.

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
sequential_time = datetime.datetime.now() - start_time
print(f"Время последовательного выполнения: {sequential_time} секунд")

#Многопроцессный вызов
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(read_info, filenames)
    parallel_time = datetime.datetime.now() - start_time
    print(f"Параллельное выполнение: {parallel_time} секунд")




