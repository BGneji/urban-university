import unittest
from unittest import TestCase
from homework_12_1 import Runner
from homework_12_2 import Tournament
import homework_12_2


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


class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = homework_12_2.Runner("Усэйн", 10)
        self.andrey = homework_12_2.Runner("Андрей", speed=9)
        self.nik = homework_12_2.Runner("Ник", speed=3)

    # @classmethod
    # def tearDownClass(cls):
    #     for result in cls.all_results.values():
    #         for key, value in result.items():
    #             print(key, value.name)
    #         print()
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        # a = tournament.start()
        # print(a.values())
        self.all_results["usain_and_nik"] = tournament.start()
        self.assertTrue(self.all_results["usain_and_nik"][max(self.all_results["usain_and_nik"])] == self.nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        self.all_results["andrey_and_nik"] = tournament.start()
        self.assertTrue(self.all_results["andrey_and_nik"][max(self.all_results["andrey_and_nik"])] == self.nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        self.all_results["usain_andrey_and_nik"] = tournament.start()
        self.assertTrue(
            self.all_results["usain_andrey_and_nik"][max(self.all_results["usain_andrey_and_nik"])] == self.nik)


TextTestRunner = unittest.TestSuite()
TextTestRunner.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
TextTestRunner.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(TextTestRunner)
