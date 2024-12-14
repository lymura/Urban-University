import sqlite3

# Открытие базы данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users, если она еще не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   age INTEGER,
                   balance INTEGER NOT NULL)''')
# Заполнение таблицы данными
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

# Проверка, есть ли записи в таблице, чтобы избежать дублирования
cursor.execute("SELECT COUNT(*) FROM Users")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users)
    connection.commit()

# Обновление баланса для каждой второй записи начиная с первой
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 0")
connection.commit()

# Удаление каждой третьей записи начиная с первой
cursor.execute("DELETE FROM Users WHERE id % 3 = 0")
connection.commit()

# Удаление записи c ID = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
connection.commit()

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(f"Общее количество записей: {total_users}")

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]
print(f"Сумма всех балансов: {all_balance}")

# Вычисление среднего баланса
if total_users > 0:
    average_balance = all_balance / total_users
    print(f"Средний баланс всех пользователей: {average_balance:.2f}")
else:
    print("Нет пользователей для расчета среднего баланса.")

# Выборка всех записей, где возраст не равен 60
select_query = """SELECT username, email, age, balance FROM Users WHERE age != 60 ORDER BY id;"""
cursor.execute(select_query)

results = cursor.fetchall()
for row in results:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

# Закрытие соединения
connection.close()
