import m_12_2
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        return cls.all_results

    def setUp(self):
        self.first = m_12_2.Runner('Усейн', 10)
        self.second = m_12_2.Runner('Андрей', 9)
        self.third = m_12_2.Runner('Ник', 3)

    def test_tournament_1(self):
        one = m_12_2.Tournament(90, self.first, self.third)
        one.start()
        self.setUpClass()

    def test_tournament_2(self):
        two = m_12_2.Tournament(90, self.second, self.third)
        two.start()
        self.setUpClass()

    def test_tournament_3(self):
        three = m_12_2.Tournament(90, self.first, self.second, self.third)
        three.start()
        self.setUpClass()

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(key, cls.all_results[key])


if __name__ == '__main__':
    unittest.main()
