# Исходные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Определение результата соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Форматирование строк с использованием %

# Строка 1
team1_str = "В команде Мастера кода участников: %d !" % team1_num

# Строка 2
teams_total_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Форматирование строк с использованием format()

# Строка 3
score_2_str = "Команда Волшебники данных решила задач: {} !".format(score_2)

# Строка 4
team2_time_str = "Волшебники данных решили задачи за {:.2f} с !".format(team2_time)

# Форматирование строк с использованием f-строк

# Строка 5
scores_str = f"Команды решили {score_1} и {score_2} задач."

# Строка 6
challenge_result_str = f"Результат битвы: {challenge_result}"

# Строка 7
tasks_total_time_avg_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

# Вывод результатов
print(team1_str)
print(teams_total_str)
print(score_2_str)
print(team2_time_str)
print(scores_str)
print(challenge_result_str)
print(tasks_total_time_avg_str)
