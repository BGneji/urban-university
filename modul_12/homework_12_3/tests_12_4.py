import logging
import unittest
from unittest import TestCase

from homework_12_3 import Runner, Tournament


class RunnerTest(TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            run_first = Runner('Вася1', 10)
            logging.info('test_walk выполнен успешно')
            for i in range(10):
                run_first.walk()
            self.assertEqual(run_first.distance, 50)
        except ValueError as exc:
            logging.warning(f"Неверная скорость для Runner {exc}")

    def test_run(self):
        try:
            second = Runner('Миша', -10)
            logging.info('test_walk выполнен успешно')
            for i in range(10):
                second.run()
            self.assertEqual(second.distance, 50)
        except TypeError as exc:
            logging.warning(f"Имя может быть только строкой, передано int {exc}")
        except ValueError as exc:
            logging.warning(f"Неверная скорость для Runner {exc}")


    # def test_challenge(self):
    #     run_first = Runner('Вася1', 10)
    #     run_second = Runner('Илья1', 10)
    #     for i in range(10):
    #         run_first.run()
    #         run_second.walk()
    #     self.assertNotEqual(run_first.distance, run_second.distance)


logging.basicConfig(level=logging.INFO, filemode='a', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s| %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()


    first = Runner('Вася', 10)
    second = Runner('Илья', 5)

    third = Runner('Арсен', 10)

    t = Tournament(100, first, second)
    print(t.start())
