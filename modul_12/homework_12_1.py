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
    def setUp(self):
        self.misha = Runner('Миша')
        self.sasha = Runner('Саша')

    def test_walk(self):
        for i in range(10):
            self.misha.walk()
        self.assertEqual(self.misha.distance, 50)

    def test_run(self):
        for i in range(10):
            self.sasha.run()
        self.assertEqual(self.sasha.distance, 100)

    def test_challenge(self):
        for i in range(10):
            self.misha.run()
            self.sasha.walk()
        self.assertNotEqual(self.misha.distance, self.sasha.distance)


if __name__ == '__main__':
    unittest.main()


