# Организация программ и методы строк.

my_string = "Это текст по умолчанию"
user_input = input("Использовать текст по умолчанию ('y')? Или ввести свой текст: ")

if user_input != 'y':
    my_string = user_input

print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ", ""))
print(my_string[0])
print(my_string[-1])
