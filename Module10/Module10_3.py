import threading
from random import randint
from time import sleep

lock = threading.Lock()


class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(1, 100):
            if lock.locked():
                lock.release()
                k = randint(50, 500)
                self.balance += k
                print(f'Пополнение: {k}. Баланс: {self.balance}')
            else:
                k = randint(50, 500)
                self.balance += k
                print(f'Пополнение: {k}. Баланс: {self.balance}')
            sleep(0.01)

    def take(self):
        for i in range(1, 100):
            k = randint(50, 500)
            print(f'Запрос на {k}')
            if self.balance >= k:
                self.balance -= k
                print(f'Снятие: {k}. Баланс: {self.balance}')
            else:
                lock.acquire()
                print('Запрос отклонён, недостаточно средств')
            sleep(0.01)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')