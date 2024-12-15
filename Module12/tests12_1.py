import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Заморозки')
    def test_walk(self):
        walker = Runner('walker')
        for i in range(0, 10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Заморозки')
    def test_run(self):
        runner = Runner('Runner1')
        for i in range(0, 10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Заморозки')
    def test_challenge(self):
        contestant1 = Runner('Cont1')
        contestant2 = Runner('Cont2')
        for i in range(0, 10):
            contestant1.walk()
            contestant2.run()
        self.assertNotEqual(contestant2.distance, contestant1.distance)