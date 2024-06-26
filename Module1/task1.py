# Практическое задание по уроку "Строки и индексация строк"
#
# • Задача: выполнить действия в PyCharm, включая запись строки в переменную, вывод первого и последнего символов,
#   вторую половину строки и вывод слова наоборот.

Text1 = "Это моя строка"
print('> Строка 1:\t\t\t', Text1)
print('Первый символ:\t\t', Text1[0])  # 0 - первый символ
print('Последний символ:\t', Text1[-1])  # -1 - последний символ
print('С 3 по 5 символы:\t', Text1[2:5])  # 2-5 - индексация строки
print('Каждый 3 символ:\t', Text1[::2])  # Каждый 3 символ 'Э_о м_я с_р_к_'
print('Строка на оборот:\t', Text1[::-1])  # -1 - индексация строки
print('Длина строки:\t\t', len(Text1))  # Длина строки

Text2 = "Это новая строка"
print('> Строка 2:\t\t\t', Text2)
print('Соединение строк:\t', Text1 + ' _ ' + Text2)  # Соединение строк
