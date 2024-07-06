# Задача "Рассылка писем":
# Функция send_email принимает 2 обычных аргумента: сообщение и получатель, а также 1 обязательно именованный аргумент
# со значением по умолчанию - отправитель.
#
# Внутри функции реализована следующая логика:
# - Проверка на корректность e-mail отправителя и получателя.
# - Проверка на отправку самому себе.
# - Проверка на отправителя по умолчанию.
#
# Если строки recipient и sender не содержат "@" или не оканчиваются на ".com"/".ru"/".net", то выводится сообщение:
# "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если sender и recipient совпадают, то выводится "Нельзя отправить письмо самому себе!"
# Если отправитель по умолчанию - university.help@gmail.com, то выводится сообщение: "Письмо успешно отправлено с
# адреса <sender> на адрес <recipient>."
# В противном случае выводится сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender>
# на адрес <recipient>."
#
# За один вызов функции выводится только одно из перечисленных уведомлений!

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
        # print(sender_error_msg)
        ...

    # Проверка получателя
    recipient_valid, recipient_error_msg = is_valid_email(recipient)
    if not recipient_valid:
        # print(recipient_error_msg)
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
# send_email('Если @ отсутствует, то письмо не отправится', 'urban.teacher.mail.ru')
