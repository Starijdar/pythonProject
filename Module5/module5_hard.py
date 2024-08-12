import time

class UrTube:
    users = {}
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        if nickname in UrTube.users:
            if hash(password) in UrTube.users[nickname]:
                if UrTube.current_user == None:
                    print(f'Добро пожаловать {nickname}')
                    UrTube.current_user = nickname
                else:
                    UrTube.log_out(self)
                    print(f'Добро пожаловать {nickname}')
                    UrTube.current_user = nickname
            else:
                print("Пароль неверный")

    def register(self, nickname, password, age, *args):
        if nickname in UrTube.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            UrTube.users[nickname] = hash(password), age
            UrTube.current_user = nickname
    def log_out(self):
        print(f'До встречи {UrTube.current_user}')
        current_user = None

    def add(self, *args):
        if str(args) in UrTube.videos:
            pass
        else:
            for i in range(len(args)):
                UrTube.videos.append(str(args[i]))

    def get_videos(self, string):
        search_list = []
        for i in UrTube.videos:
            if string.lower() in i.lower():
                search_list.append(i)
        return search_list
    def watch_video(self, title):
        if UrTube.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif title in UrTube.videos:
            if True in Video.videos[title]:
                if UrTube.users[self.current_user][1] < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for Video.time_now in range(1, Video.videos[title][0] + 1):
                        # time.sleep(1)
                        print(Video.time_now, end=' ')
                    print('Конец видео')
                    Video.time_now = 0
            else:
                print('можно')


class Video:
    adult_mode = False
    time_now = 0
    videos = {}
    def __new__(cls, *args, **adult_mode):
        cls.videos[args[0]] = args[1], bool(adult_mode)
        return super().__new__(cls)

    def __init__(self, title, duration, **adult_mode):
        self.title = title
        self.duration = duration
        if adult_mode:
            self.adult_mode = True

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    # def __contains__(self, item):
    #     if item.lower in self.title.lower():
    #         pass



class User:

    def __init__(self, *args):
        self.nickname = UrTube.current_user
        self.password = UrTube.users[self.nickname][0]
        self.age = UrTube.users[self.nickname][1]

    def __str__(self):
        return f"Пользователь: {self.nickname}, возраст: {self.age}"

    def __repr__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"


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


ur.log_in('vasya_pupkin', 'lolkekcheburek')


us = User()
print(us)
