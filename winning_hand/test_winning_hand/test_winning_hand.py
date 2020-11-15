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

    def test_ace_high_vs_double_king_vs_two_pair(self):
        hand1, hand2, hand3 = 'As 3h 8c 4d 5s', 'Kd Qd Ks 7c 5c', '2d 3d 2s 3c 4c'
        expected = '(Diamond 2, Diamond 3, Spade 2, Club 3, Club 4)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3)))

    def test_double_ace_vs_triple_2_vs_two_pair(self):
        hand1, hand2, hand3 = 'As Ah 8c 4d 5s', '2d 4s 2s 7c 2c', 'Kd Qd Ks Qc 5c'
        expected = '(Diamond 2, Spade 4, Spade 2, Club 7, Club 2)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3)))

    def test_triple_ace_vs_two_pair_vs_wheel(self):
        hand1, hand2, hand3 = 'As Ah Ac 4d 5s', '2h 4s 2s 7c 2c', 'Ad 2d 3s 4c 5h'
        expected = '(Diamond A, Diamond 2, Spade 3, Club 4, Heart 5)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3)))

    def test_triple_ace_vs_wheel_vs_straight(self):
        hand1, hand2, hand3 = 'As Ah Ac 4d 5s', '2s 4s 3h 5c 6h', 'Ad 2d 3s 4c 5h'
        expected = '(Spade 2, Spade 4, Heart 3, Club 5, Heart 6)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3)))

    def test_wheel_vs_straight_vs_flush(self):
        hand1, hand2, hand3 = 'Ad 2d 3s 4c 5h', '2s 4s 3h 5c 6h', 'Kd 2d 3d 4d 5d'
        expected = '(Diamond K, Diamond 2, Diamond 3, Diamond 4, Diamond 5)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3)))

    def test_straight_vs_flush_vs_full_house(self):
        hand1, hand2, hand3 = '2s 4s 3h 5c 6h', 'Kd 2d 3d 4d 5d', '2d 5d 2s 2c 5h'
        expected = '(Diamond 2, Diamond 5, Spade 2, Club 2, Heart 5)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3)))

    def test_straight_vs_flush_vs_full_house_vs_quad(self):
        hand1, hand2, hand3, hand4 = '2s 4s 3h 5c 6h', 'Kd 2d 3d 4d 5d', '2d 5d 2s 2c 5h', '7d 7h 7c 7s 2d'
        expected = '(Diamond 7, Heart 7, Club 7, Spade 7, Diamond 2)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3, hand4)))

    def test_quad_vs_flush_vs_full_house_vs_wheel_flush(self):
        hand1, hand2, hand3, hand4 = '7d 7h 7c 7s 2d', 'Kd 2d 3d 4d 5d', '2d 5d 2s 2c 5h', 'As 2s 4s 3s 5s'
        expected = '(Spade A, Spade 2, Spade 4, Spade 3, Spade 5)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3, hand4)))

    def test_quad_vs_flush_vs_quad_vs_wheel_flush_vs_straight_flush(self):
        hand1, hand2, hand3, hand4 = '7d 7h 7c 7s 2d', 'Kd 2d 3d 4d 5d', 'As 2s 4s 3s 5s', '4s 3s 5s 6s 7s'
        expected = '(Spade 4, Spade 3, Spade 5, Spade 6, Spade 7)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3, hand4)))

    def test_royal_flush(self):
        hand1, hand2, hand3, hand4 = '7d 7h 7c 7s 2d', 'Kd 2d 3d 4d 5d', 'As 2s 4s 3s 5s', 'Ks Qs Js 10s 9s'
        royal_hand, expected = 'Ah Kh Qh Jh 10h', '(Heart A, Heart K, Heart Q, Heart J, Heart 10)'
        self.assertEqual(expected, str(winning_hand(hand1, hand2, hand3, hand4, royal_hand)))


if __name__ == '__main__':
    unittest.main()
