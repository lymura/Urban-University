
from datetime import datetime
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Measure time for sequential execution
start_time = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = datetime.now()
time_res = end_time - start_time

print(f"Время выполнения функций: {time_res} секунд")

# Measure time for parallel execution using threads
start_time = datetime.now()

threads = [
    Thread(target=write_words, args=(10, 'example5.txt')),
    Thread(target=write_words, args=(30, 'example6.txt')),
    Thread(target=write_words, args=(200, 'example7.txt')),
    Thread(target=write_words, args=(100, 'example8.txt'))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = datetime.now()
time_res = end_time - start_time

print(f"Работа потоков: {time_res} секунд")
