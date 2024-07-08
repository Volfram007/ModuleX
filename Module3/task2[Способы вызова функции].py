def send_email(message, recipient, sender='university.help@gmail.com'):
    # Проверка на корректность e-mail отправителя и получателя.
    def is_valid_email(email):
        if "@" not in email:
            return False, f'Адрес {email} не содержит символа "@"'

        domain = email.split("@")[1]  # Проверка на принадлежность e-mail.
        if not domain.endswith((".com", ".ru", ".net")):  # Проверка на допустимые домены.
            return False, f'Адрес {email} не заканчивается на ".com", ".ru" или ".net"'
        return True, ""

    # Проверка отправителя
    sender_valid, sender_error_msg = is_valid_email(sender)
    if not sender_valid:
        # print('\033[33msender_valid:\033[0m', sender_error_msg)
        ...

    # Проверка получателя
    recipient_valid, recipient_error_msg = is_valid_email(recipient)
    if not recipient_valid:
        # print('\033[33mrecipient_valid:\033[0m', recipient_error_msg)
        ...

    # Проверка на отправку самому себе.
    if not sender_valid or not recipient_valid:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на отправку самому себе.
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return

    # Проверка на отправителя по умолчанию.
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса "{sender}" на адрес "{recipient}"')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "{sender}" на адрес "{recipient}"')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Если @ отсутствует, то письмо не отправится', 'urban.teacher.mail.ru')

'''
**Задача "Рассылка писем"**
Создайте функцию `send_email`, которая принимает 2 обычных аргумента: `message` (сообщение), `recipient` (получатель), и 
1 именованный аргумент со значением по умолчанию `sender = "university.help@gmail.com"`.

**Логика функции:**
1. Проверка на корректность e-mail отправителя и получателя.
2. Проверка на отправку самому себе.
3. Проверка на отправителя по умолчанию.

**Пункты задачи:**
1. Создайте функцию `send_email` с аргументами `message`, `recipient` и `sender="university.help@gmail.com"`.
2. Если `recipient` или `sender` не содержит "@" или не оканчивается на ".com"/".ru"/".net", вывести: 
   - "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
3. Если `sender` и `recipient` совпадают, вывести: 
   - "Нельзя отправить письмо самому себе!".
4. Если `sender` равен "university.help@gmail.com", вывести: 
   - "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
5. В противном случае вывести: 
   - "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>." 
'''
