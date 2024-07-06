from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age  # Возраст

    def __str__(self):
        return f"User: {self.nickname}, Password: {self.password}, Age: {self.age}"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users_list = []
        self.videos_list = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users_list:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        # Добавляем нового пользователя в список
        self.users_list.append(User(nickname, hash(password), age))
        # print(f'{nickname} успешно зарегистрирован!')

    def log_in(self, login, password):
        if self.current_user is None:
            for user in self.users_list:
                if user.nickname == login and user.password == hash(password):
                    self.current_user = user
                    # print(f"Вы вошли как {user.nickname}")
                    return
            print("Неверный логин или пароль", )
            return
        print("Вы уже вошли в аккаунт")

    def log_out(self):
        if self.current_user is None:
            print("Вы не входили в аккаунт")
            return
        # print(f"{self.current_user.nickname} Вы вышли с аккаунта")
        self.current_user = None

    def add(self, *video_lst):
        for video in video_lst:
            if video.title not in [v.title for v in self.videos_list]:  # Перебор списка и сравнения названий
                self.videos_list.append(video)
            else:
                print(f'Видео "{video.title}" уже существует')

    def get_videos(self, search_word):
        result = []
        for video in self.videos_list:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        for video in self.videos_list:
            if video.title == title:
                if self.current_user.age < 18 and video.adult_mode:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                print('Воспроизведение:', end=' ')
                for second in range(video.duration):
                    sleep(0.25)
                    print(second + 1, end=' ')
                return print('Конец видео')
        print('Видео не найдено')


ur = UrTube()

# рег акк
ur.register('user1', 'pass1', 12)
ur.register('user2', 'pass2', 18)
ur.register('vasya_pupkin', 'не дорос', 10)
# ап видео
v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего девушкам парень программист?', 10, True)
ur.add(v1, v2)

# Проверка поиска видео
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.log_in('user1', 'pass1')
ur.watch_video('Для чего девушкам парень программист?')
ur.log_out()
ur.log_in('user2', 'pass2')
ur.watch_video('Для чего девушкам парень программист?')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Регистрация нового пользователя с существующим в БД
ur.register('vasya_pupkin', 'не дорос', 10)

# Вывод информации о пользователе под которым работаем
print('\n\t\t', ur.current_user)
'''
### Задание "Свой YouTube"
Реализуйте три класса: `UrTube`, `Video`, `User`.

#### Подробное ТЗ:
**Класс User:**
- Атрибуты: `nickname` (строка), `password` (число, хэш), `age` (число).
**Класс Video:**
- Атрибуты: `title` (строка), `duration` (число, секунды), `time_now` (число, начальное значение 0), 
`adult_mode` (bool, по умолчанию False).

**Класс UrTube:**
- Атрибуты: `users` (список объектов User), `videos` (список объектов Video), `current_user` (объект User).
- Метод `log_in(nickname, password)`: находит пользователя по логину и паролю, устанавливает `current_user`.
- Метод `register(nickname, password, age)`: добавляет пользователя, если его нет. Выводит сообщение при попытке 
регистрации существующего пользователя.
- Метод `log_out()`: сбрасывает `current_user` на None.
- Метод `add(*videos)`: добавляет видео, если с таким названием видео еще нет.
- Метод `get_videos(keyword)`: возвращает список названий видео, содержащих ключевое слово (без учета регистра).
- Метод `watch_video(title)`: воспроизводит видео, если пользователь авторизован и нет возрастных ограничений. 
Выводит сообщения о статусе воспроизведения и ограничениях.

Для проверки:
```python
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
```

Ожидаемый вывод: 
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует  
'''