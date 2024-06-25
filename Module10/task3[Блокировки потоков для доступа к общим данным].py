# Задание:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации общего
# ресурса.
# Примечание:
# Используйте класс Lock из модуля threading для блокировки доступа к общему ресурсу. Ожидается создание
# двух потоков, один для пополнения счета, другой для снятия денег. Используйте with (lock object):
# в начале каждого метода, чтобы использовать блокировку.

from threading import Thread, Lock


class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:  # Блокируем доступ
            new_balance = self.balance + amount
            print(f"Пополнение на {amount}, новый баланс {new_balance}")
            self.balance = new_balance  # Обновляем баланс

    def withdraw(self, amount):
        with self.lock:  # Блокируем доступ
            if self.balance >= amount:
                new_balance = self.balance - amount
                print(f"Снимаем {amount}, новый баланс {new_balance}")
                self.balance = new_balance  # Обновляем баланс
            else:
                print(f"Не удалось вывести средства {amount}, баланс {self.balance}")


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
