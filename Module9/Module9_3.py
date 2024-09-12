import time

start_time = time.time()

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (True if len(first[x]) > len(second[x]) else False for x in range(0, 3))

print(list(first_result))
print(list(second_result))


finish_time = time.time()
print(f'Время выполнения в секундах {(finish_time-start_time) * 1000}')
