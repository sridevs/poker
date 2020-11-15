from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestStraightFlush(TestCase):

    def setUp(self) -> None:
        self.quad_ace = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart K', 'Heart A'
        ))
        self.ace_full_house = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart K', 'Diamond K'
        ))
        self.ace_flush = create_mock_cards((
            'Heart A', 'Heart K', 'Heart Q', 'Heart J', 'Heart 9'
        ))
        self.low_straight_flush = create_mock_cards((
            'Club 2', 'Club 3', 'Club 4', 'Club 5', 'Club 6'
        ))
        self.broadway = create_mock_cards((
            'Diamond A', 'Club K', 'Spade Q', 'Heart J', 'Diamond 10'
        ))
        self.wheel_flush = create_mock_cards((
            'Club A', 'Club 2', 'Club 3', 'Club 4', 'Club 5'
        ))
        self.diamond_straight_six_flush = create_mock_cards((
            'Diamond 6', 'Diamond 2', 'Diamond 3', 'Diamond 4', 'Diamond 5'
        ))
        self.straight_queen_flush = create_mock_cards((
            'Heart Q', 'Heart 8', 'Heart J', 'Heart 10', 'Heart 9'
        ))
        self.straight_King_flush = create_mock_cards((
            'Heart Q', 'Heart K', 'Heart J', 'Heart 10', 'Heart 9'
        ))
        self.royal_flush = create_mock_cards((
            'Spade Q', 'Spade K', 'Spade J', 'Spade 10', 'Spade A'
        ))

    def test_low_straight_flush_is_greater_than_quad_ace(self):
        hand1, hand2 = Hand(self.low_straight_flush), Hand(self.quad_ace)
        self.assertGreater(hand1, hand2)

    def test_low_straight_flush_is_greater_than_full_house(self):
        hand1, hand2 = Hand(self.low_straight_flush), Hand(self.ace_full_house)
        self.assertGreater(hand1, hand2)

    def test_low_straight_flush_is_greater_than_ace_flush(self):
        hand1, hand2 = Hand(self.low_straight_flush), Hand(self.ace_flush)
        self.assertGreater(hand1, hand2)

    def test_low_straight_flush_is_greater_than_wheel_flush(self):
        hand1, hand2 = Hand(self.low_straight_flush), Hand(self.wheel_flush)
        self.assertGreater(hand1, hand2)

    def test_low_straight_flush_is_equal_to_similar_flush(self):
        hand1, hand2 = Hand(self.low_straight_flush), Hand(self.diamond_straight_six_flush)
        self.assertEqual(hand1, hand2)

    def test_wheel_flush_is_greater_than_quad_ace(self):
        hand1, hand2 = Hand(self.wheel_flush), Hand(self.quad_ace)
        self.assertGreater(hand1, hand2)

    def test_wheel_flush_is_greater_than_broadway(self):
        hand1, hand2 = Hand(self.wheel_flush), Hand(self.broadway)
        self.assertGreater(hand1, hand2)

    def test_wheel_flush_is_less_than_low_straight_flush(self):
        hand1, hand2 = Hand(self.wheel_flush), Hand(self.low_straight_flush)
        self.assertLess(hand1, hand2)

    def test_straight_queen_flush_is_greater_than_straight_six_flush(self):
        hand1, hand2 = Hand(self.straight_queen_flush), Hand(self.diamond_straight_six_flush)
        self.assertGreater(hand1, hand2)

    def test_queen_straight_flush_is_less_than_king_straight_flush(self):
        hand1, hand2 = Hand(self.straight_queen_flush), Hand(self.straight_King_flush)
        self.assertLess(hand1, hand2)

    def test_royal_flush_is_greater_than_king_straight_flush(self):
        hand1, hand2 = Hand(self.royal_flush), Hand(self.straight_King_flush)
        self.assertGreater(hand1, hand2)


if __name__ == '__main__':
    main()
