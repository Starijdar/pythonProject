import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest():
    def test_walk(self):
        try:
            runner = Runner('Вася', -5)
        except ValueError as err:
            logging.warning(f'Скорость не может быть отрицательной')
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(12, -5)
        except TypeError as err:
            logging.warning(f'Неверный тип данных для объекта Runner')
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(levelname)s | %(message)s")

runner_test = RunnerTest()
runner_test.test_walk()
runner_test.test_run()