import unittest
import RunnersTornament as Rt


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = Rt.Runner('Усэйн', 10)
        self.runer_2 = Rt.Runner('Андрей', 9)
        self.runer_3 = Rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_run1(self):
        run_1 = Rt.Tournament(90, self.runer_1, self.runer_3)
        result = run_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним')
        self.all_results['test_run1'] = result

    def test_run2(self):
        run_2 = Rt.Tournament(90, self.runer_2, self.runer_3)
        result = run_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним')
        self.all_results['test_run2'] = result

    def test_run3(self):
        run_3 = Rt.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = run_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним')
        self.all_results['test_run3'] = result

    def test_run4(self):
        run_4 = Rt.Tournament(6, self.runer_1, self.runer_2, self.runer_3)
        result = run_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним')
        self.all_results['test_run4'] = result

if __name__ == '__main__':
        unittest.main()
