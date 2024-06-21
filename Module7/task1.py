# Режимы открытия файлов

f_name = 'test.txt'
file = open(f_name, mode='r', encoding='utf-8')
print(file.read())
file.close()
