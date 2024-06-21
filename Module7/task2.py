# Оператор "with"
with open('test.txt', mode='r', encoding='utf-8') as file:
    print(file.read())

if file.closed:
    print('\nФайл закрыт ранее'.upper())
    