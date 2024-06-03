# # Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы,
# где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.).
# Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.
#
# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут
# выполнять похожий функционал на сайте.
#
# Всего будет 3 класса: UrTube, Video, User.
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платоформой, каждый из которых будет содержать методы добавления видео,
# авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с такмими же логином и паролем.
# Если такой пользователь суещствует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же следует учитывать следущие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"

from time import sleep


class UrTube:
    def __init__(self):
        self.data = {}
        self.videos = []
        self.current_user = None

    def __str__(self):
        return f'{self.videos}'



    def register(self, username, password, age):
        if not self.data.get(username, False):
            self.data[username] = []
            self.data[username].append(hash(password))
            self.data[username].append(age)
            self.log_in(username, password, age)

            return [username, password, age]
        else:
            print(f'Пользователь {username} уже существует')
            self.current_user = True
            return [username, password, self.data[username][1]]

    def log_in(self, username, password, age=None):
        if self.data.get(username, False) and self.data[username][0] == hash(password):
            print(f'Добро пожаловать {username}')
            if age is None:
                age = self.data[username][1]
                
            self.current_user = [username, age]
            print(self.current_user)
            return self.current_user
        elif self.data.get(username, False) and self.data[username][0] != hash(password):
            print('Пароль не верный')
        else:
            print('Такого логина нет, требуется регистрация')

    def log_out(self):
        if not self.current_user:
            # print(self.current_user)
            print('Вы не залогинились')
        elif self.current_user:
            self.current_user = None
            # print(self.current_user)
            print('Разлогинится')

    def add_video(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f'{video.title}')
            else:
                print(f'{video.title} Такое видео уже существует')

    def get_video(self, name):
        get_ = {}
        for i in range(len(self.videos)):
            if name.lower() in self.videos[i].title.lower():
                get_[self.videos[i].title] = self.videos[i].duration
        return get_
    def watch_video(self, name_video):
        if self.get_video(name_video):
            if not self.current_user:
                print('Войдите в аккаунт чтобы смотреть видео')
                print(self.current_user[1])
            elif self.current_user[1] > 18:
                var = self.get_video(name_video).get(name_video)
                for i in range(1, var + 1):
                    print(i, end=' ')
                    sleep(1)
                else:
                    print('Конец видео!')
                    sleep(1)
            elif self.current_user[1] < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')

        elif not self.get_video(name_video):
            print("Такого видео нет")


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class User:
    def __init__(self, nickname: str, password, age: int = None):
        self.nickname = nickname
        self.password = password
        self.age = age


if __name__ == '__main__':
    database = UrTube()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n3 - Выход\n4 - Добавить "
                           "видео\n5 - Поиск видео\n6 - Смотреть видео\n7 - Выход\n"))
        print('*' * 10)
        if choice == 1:
            user = User(input('Введите логин: '), password := input('Введите пароль: '))
            database.log_in(user.nickname, user.password)
        elif choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        age := int(input('Введите возрост: ')))
            database.register(user.nickname, user.password, age)
        elif choice == 3:
            UrTube.log_out(database)
        elif choice == 4:
            v1 = Video('Лучший язык программирования 2024 года', 200)
            v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
            database.add_video(v1, v2)
            # for i in database.videos:
            #     print(i)
        elif choice == 5:
            if not database.videos:
                print('В UrTube нет загруженных видео')
            else:
                search = input('Какое видео хотите найти? ')
                list_ = list(database.get_video(search).keys())
                print(list_)

        elif choice == 6:
            if not database.videos:
                print('В UrTube нет загруженных видео')
            else:
                database.watch_video('Для чего девушкам парень программист?')
            # database.watch_video('аацпймуиа')
        elif choice == 7:
            break

        print('*' * 10)
        # print(database.data)
