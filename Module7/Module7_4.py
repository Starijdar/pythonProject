team1_num = input("Сколько участников в команде 1? ")
print('В команде Мастера кода участников: %s!' %team1_num)
team2_num = input("Сколько участников в команде 2? ")
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

score_1 = int(input("Сколько задач решила команда 1? "))
score_2 = int(input("Сколько задач решила команда 2? "))

print('Команда Волшебники данных решила задач: {} !'.format(score_2))

team1_time = int(input('Время за которое команда 1 решила задачи в секундах '))
team2_time = int(input('Время за которое команда 2 решила задачи в секундах '))
print("Волшебники данных решили задачи за {} с !".format(float(team2_time)))

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

if result == 'Ничья!':
    print(f'{result}')
else:
    print(f'Результат битвы: {result}')

task_total = score_2 + score_1

time_avg = (team1_time + team2_time) / task_total

print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!.')