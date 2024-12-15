import tests12_2
import RunnersTornament
import tests12_1
import unittest

testTS = unittest.TestSuite()
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_2.TournamentTest))
testTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testTS)