import queue
import threading
from time import sleep
from queue import Queue
from random import randint

lock = threading.Lock()
q = queue.Queue()


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(1, 1))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        for g in guests:
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    print(f'{g.name} сел(-а) за стол номер {t.number}')
                    g.start()
                    break
                else:
                    continue
            else:
                q.put(g)
                print(f'{g.name} в очереди')

    def discuss_guests(self):
        while not q.empty():
            for t in self.tables:
                if t.guest is None and not q.empty():
                    t.guest = q.get()
                    print(f'{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')
                    t.guest.start()
                elif t.guest is not None and t.guest.is_alive():
                    continue
                else:
                    print(f'{t.guest.name} покушал(-а) и ушёл(ушла)')
                    t.guest = None
                    print(f'Стол номер {t.number} свободен')

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
