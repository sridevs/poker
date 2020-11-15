from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestHandPair(TestCase):

    def setUp(self) -> None:
        self.ace_king_high = create_mock_cards((
            'Club K', 'Spade 2', 'Diamond 3', 'Diamond 4', 'Heart A'
        ))
        self.double_ace = create_mock_cards((
            'Club A', 'Spade 2', 'Diamond J', 'Diamond 4', 'Heart A'
        ))
        self.double_ace_similar = create_mock_cards((
            'Diamond A', 'Club J', 'Spade A', 'Heart 4', 'Diamond 2'
        ))
        self.double_ace_king_high = create_mock_cards((
            'Diamond K', 'Club A', 'Spade 3', 'Heart A', 'Diamond 6'
        ))
        self.double_King_Queen_high = create_mock_cards((
            'Diamond K', 'Club Q', 'Spade K', 'Heart J', 'Diamond 10'
        ))
        self.double_ace_low = create_mock_cards((
            'Diamond 2', 'Club A', 'Spade 3', 'Heart 4', 'Diamond A'
        ))
        self.double_5 = create_mock_cards((
            'Diamond 5', 'Club 2', 'Spade 3', 'Heart 5', 'Diamond 7'
        ))
        self.double_2 = create_mock_cards((
            'Diamond 2', 'Club 2', 'Spade 3', 'Heart 5', 'Diamond 7'
        ))
        self.double_5_ace_high = create_mock_cards((
            'Diamond 5', 'Club 2', 'Spade 3', 'Heart 5', 'Diamond A'
        ))
        self.double_J = create_mock_cards((
            'Diamond J', 'Club 2', 'Spade 3', 'Diamond 5', 'Heart J'
        ))

    def test_double_ace_is_greater_than_ace_king_high(self):
        hand1, hand2 = Hand(self.double_ace), Hand(self.ace_king_high)
        self.assertGreater(hand1, hand2)

    def test_double_two_is_greater_than_ace_king_high(self):
        hand1, hand2 = Hand(self.double_2), Hand(self.ace_king_high)
        self.assertGreater(hand1, hand2)

    def test_equality_of_similar_double_ace(self):
        hand1, hand2 = Hand(self.double_ace), Hand(self.double_ace_similar)
        self.assertEqual(hand1, hand2)

    def test_double_ace_king_high_is_greater_than_double_ace(self):
        hand1, hand2 = Hand(self.double_ace_king_high), Hand(self.double_ace)
        self.assertGreater(hand1, hand2)

    def test_double_ace_low_is_greater_than_double_King_queen_high(self):
        hand1, hand2 = Hand(self.double_ace_low), Hand(self.double_King_Queen_high)
        self.assertGreater(hand1, hand2)

    def test_double_J_is_greater_than_double_5(self):
        hand1, hand2 = Hand(self.double_J), Hand(self.double_5)
        self.assertGreater(hand1, hand2)

    def test_double_J_is_greater_than_double_5_ace_high(self):
        hand1, hand2 = Hand(self.double_J), Hand(self.double_5_ace_high)
        self.assertGreater(hand1, hand2)

    def test_double_5_is_lesser_than_double_5_ace_high(self):
        hand1, hand2 = Hand(self.double_5), Hand(self.double_5_ace_high)
        self.assertLess(hand1, hand2)

    def test_double_2_is_lesser_than_double_5(self):
        hand1, hand2 = Hand(self.double_2), Hand(self.double_5)
        self.assertLess(hand1, hand2)


if __name__ == '__main__':
    main()
