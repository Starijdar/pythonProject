from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'


print(list(map(lambda x, y: bool(x == y), first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        for i in data_set:
            if isinstance(i, str):
                with open(file_name, 'a', encoding='UTF-8') as file:
                    file.write(i + '\n')
            elif isinstance(i, list):
                with open(file_name, 'a', encoding='UTF-8') as file:
                    file.write(str(i) + '\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *some_words):
        self.words = some_words

    def __call__(self, *args, **kwargs):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Nope', 'Вполне')
print(first_ball())
print(first_ball())
print(first_ball())
