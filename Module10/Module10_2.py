import threading
from threading import Thread
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100
        self.counter = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()
        print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')


    def fight(self):
        while self.enemy:
            self.counter += 1
            self.enemy -= self.power
            print(f'{self.name} сражается {self.counter}..., осталось {self.enemy} воинов.')
            sleep(1)


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончены!')