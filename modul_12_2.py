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
        self.all_results[1] = one.start()


    def test_tournament_2(self):
        two = m_12_2.Tournament(90, self.second, self.third)
        self.all_results[2] = two.start()

    def test_tournament_3(self):
        three = m_12_2.Tournament(90, self.first, self.second, self.third)
        self.all_results[3] = three.start()




    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)


if __name__ == '__main__':
    unittest.main()
