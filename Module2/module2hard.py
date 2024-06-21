from random import randint


def cipher(arg):
    result = ''
    for i in range(1, arg):
        for j in range(i + 1, arg):
            # if i + j == arg:
            if arg % (i + j) == 0:
                result += str(i) + str(j)  # + ' '
    return result


while True:
    num = input('Введите число от 3 до 20 или жми Enter\n\t(0 - выход): ')
    if num == '0':
        break
    if num == '':
        num = randint(3, 20)
    elif int(num) < 3 or int(num) > 20:
        print("Неверное число. Введите число от 3 до 20!!!")
        continue
    else:
        num = int(num)
    print(num, '-', cipher(int(num)))
