import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for dep in range(100):
            refill = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += refill
            print(f'Пополнение: {refill}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for ta in range(100):
            get = randint(50, 500)
            print(f'Запрос на: {get}.')
            if get <= self.balance:
                self.balance -= get
                print(f'Снятие: {get}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
