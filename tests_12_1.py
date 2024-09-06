import unittest
from RunnerTest12_1 import Runner


class RunnerTest(unittest.TestCase):

    def test_run(self):
        runner = Runner('Ivan')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_walk(self):
        runner = Runner('Masha')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
        self.assertEqual(runner.distance, 30)

    def test_challenge(self):
        runner1 = Runner('Igor')
        runner2 = Runner('Yulia')

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
