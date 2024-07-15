from threading import Thread, Lock


class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:  # Блокируем доступ
            self.balance += amount
            print(f"Пополнение на {amount}, новый баланс {self.balance}")

    def withdraw(self, amount):
        with self.lock:  # Блокируем доступ
            if self.balance >= amount:
                self.balance -= amount
                print(f"Снимаем {amount}, новый баланс {self.balance}")
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

# ### Задание "Блокировки и обработка ошибок"
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# #### Требования:
# 1. Создайте класс `BankAccount` с атрибутом баланса и методами для пополнения и снятия денег.
# 2. Используйте блокировку (`Lock` из модуля `threading`) для предотвращения гонок при модификации баланса.
# 3. Создайте два потока: один для пополнения счета, другой для снятия денег.
#
#
# #### Примечание:
# Используйте `with self.lock:` в начале каждого метода для блокировки доступа к балансу.
