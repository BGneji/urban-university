import unittest
from unittest import TestCase


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


class RunnerTest(TestCase):
    def test_walk(self):
        new_obj = Runner('Миша')
        for i in range(10):
            new_obj.walk()
        self.assertEqual(new_obj.distance, 50)

    def test_run(self):
        new_obj = Runner('Саша')
        for i in range(10):
            new_obj.run()
        self.assertEqual(new_obj.distance, 100)

    def test_challenge(self):
        new_obj_one = Runner('Миша')
        new_obj_two = Runner('Саша')
        for i in range(10):
            new_obj_one.run()
            new_obj_two.walk()

        self.assertNotEqual(new_obj_one.distance, new_obj_two.distance)


if __name__ == '__main__':
    unittest.main()


