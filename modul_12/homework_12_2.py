import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            for key, value in result.items():
                print(key, value.name)
            print()

    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        # a = tournament.start()
        # print(a.values())
        self.all_results["usain_and_nik"] = tournament.start()
        self.assertTrue(self.all_results["usain_and_nik"][max(self.all_results["usain_and_nik"])] == self.nik)

    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        self.all_results["andrey_and_nik"] = tournament.start()
        self.assertTrue(self.all_results["andrey_and_nik"][max(self.all_results["andrey_and_nik"])] == self.nik)

    def test_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        self.all_results["usain_andrey_and_nik"] = tournament.start()
        self.assertTrue(
            self.all_results["usain_andrey_and_nik"][max(self.all_results["usain_andrey_and_nik"])] == self.nik)


if __name__ == '__main__':
    unittest.main()
