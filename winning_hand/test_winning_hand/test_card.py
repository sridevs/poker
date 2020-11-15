import unittest

from models.card import Card


class TestCard(unittest.TestCase):

    def test_cards_with_same_suite_and_value_are_equal(self):
        card1, card2 = Card('5C'), Card('5C')
        self.assertEqual(card1, card2)

    def test_cards_with_diff_suite_and_value_are_equal(self):
        card1, card2 = Card('5S'), Card('5C')
        self.assertEqual(card1, card2)

    def test_cards_with_same_suite_and_diff_value_are_not_equal(self):
        card1, card2 = Card('5C'), Card('4C')
        self.assertNotEqual(card1, card2)

    def test_cards_with_diff_value_and_suite_are_not_equal(self):
        card1, card2 = Card('5C'), Card('3D')
        self.assertNotEqual(card1, card2)

    def test_max_of_higher_card_same_suite(self):
        card1, card2 = Card('5C'), Card('3C')
        self.assertGreater(card1, card2)

    def test_max_of_higher_card_diff_suite(self):
        card1, card2 = Card('5C'), Card('3D')
        self.assertGreater(card1, card2)

    def test_min_of_lower_card_same_suite(self):
        card1, card2 = Card('KC'), Card('2C')
        self.assertLess(card2, card1)

    def test_min_of_lower_card_diff_suite(self):
        card1, card2 = Card('AC'), Card('2H')
        self.assertLess(card2, card1)


if __name__ == '__main__':
    unittest.main()
