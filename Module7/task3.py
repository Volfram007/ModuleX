from random import randint, uniform

# Генерация случайного количества участников для каждой команды
team1_num = randint(5, 10)
team2_num = randint(5, 10)
# Генерация случайного количества решенных задач для каждой команды
score_1 = randint(44, 77)
score_2 = randint(44, 77)
# Генерация случайного времени решения для каждой команды (с точкой)
team1_time = uniform(1400, 2100)
team2_time = uniform(1500, 2200)

# Подсчет общего количества решенных задач
tasks_total = score_1 + score_2
# Расчет среднего времени решения задач
time_avg = (team1_time + team2_time) / 2

# Определение победителя на основе количества решенных задач и времени
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Мастера кода'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Волшебники Данных'
else:
    result = 'Ничья'
challenge_result = result

# Примеры с использованием %
result1 = 'В команде "%s" участников: %d !' % (challenge_result, team1_num)
result2 = 'Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num)

# Примеры с использованием format()
result3 = 'Команда "{}" решила задач: {} !'.format(challenge_result, score_2)
result4 = '"{}" решили задачи за {:.3f} с !'.format(challenge_result, team2_time)

# Примеры с использованием f-строк
result5 = f'Команды решили {score_1} и {score_2} задач.'
result6 = f'Результат битвы: {challenge_result}'
result7 = f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.3f} секунды на задачу!'

# Вывод заголовка с именем победителя, отцентрированного в строке шириной 45 символов
print('{txt:^45}'.format(txt='Победитель ' + result.upper() + ' !'))
# Вывод всех сформированных результатов
for i in range(1, 8):
    print(eval(f"result{i}"))
