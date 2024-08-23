import unittest
from unittest import TestCase
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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(TestCase):
    is_frozen = False

    def setUp(self):
        self.misha = Runner('Миша')
        self.sasha = Runner('Саша')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
    first = Runner('Вася', 10)
    second = Runner('Илья', 5)
    # third = Runner('Арсен', 10)

    t = Tournament(0, first, second)
    print(t.start())
    logging.debug('s')
    logging.info('d')
    logging.warning("f")
    logging.error('f')
    logging.error('f')