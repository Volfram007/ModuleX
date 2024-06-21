# Базовые структуры данных.

# Дополнительное практическое задание по модулю: "Базовые структуры данных"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Hendrik', 'Aaron'}

# Сортируем по алфавиту
students = sorted(students)

# Перебор списка
for students_list, grades_list in zip(students, grades):
    # Вычисляем средний балл и выводим результат
    print(students_list, sum(grades_list) / len(grades_list))
