import unittest

from winning_hand import winning_hand


class TestWinningHand(unittest.TestCase):

    def test_ace_high_vs_king_high(self):
        hand1, hand2 = '2s 3h 8c Jd As', '2d 3d 8s Jc Kc'
        expected = '(Spade 2, Heart 3, Club 8, Diamond J, Spade A)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2)))

    def test_king_high_vs_queen_high(self):
        hand1, hand2 = '2s 3h 8c Jd Ks', '2d 3d 8s Jc Qc'
        expected = '(Spade 2, Heart 3, Club 8, Diamond J, Spade K)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2)))

    def test_Queen_high_vs_Jack_high(self):
        hand1, hand2 = '2s 3h 8c Jd Qs', '2d 3d 8s Jc 10c'
        expected = '(Spade 2, Heart 3, Club 8, Diamond J, Spade Q)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2)))

    def test_Jack_high_vs_10_high(self):
        hand1, hand2 = '2s 3h 8c Jd 6s', '2c 3d 8s 4c 9d'
        expected = '(Spade 2, Heart 3, Club 8, Diamond J, Spade 6)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2)))

    def test_8_high_vs_7_high(self):
        hand1, hand2 = '2s 3h 8c 4d 5s', '2d 3d 6s 7c 5c'
        expected = '(Spade 2, Heart 3, Club 8, Diamond 4, Spade 5)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2)))


if __name__ == '__main__':
    unittest.main()
