from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestHandHighCard(TestCase):

    def setUp(self) -> None:
        self.heart_ace_king_high = create_mock_cards((
            'Club K', 'Spade 2', 'Diamond 3', 'Diamond 4', 'Heart A'
        ))
        self.diamond_ace_king_high = create_mock_cards((
            'Diamond K', 'Club 2', 'Spade 3', 'Heart 4', 'Diamond A'
        ))
        self.diamond_ace_queen_high = create_mock_cards((
            'Diamond Q', 'Club 2', 'Spade 3', 'Heart 4', 'Diamond A'
        ))
        self.king_queen_high = create_mock_cards((
            'Diamond K', 'Club Q', 'Spade 10', 'Heart 9', 'Diamond 7'
        ))
        self.ace_6_high = create_mock_cards((
            'Diamond A', 'Club 2', 'Spade 3', 'Heart 4', 'Diamond 6'
        ))
        self.lowest_rank = create_mock_cards((
            'Diamond 5', 'Club 2', 'Spade 3', 'Heart 4', 'Diamond 7'
        ))

    def test_ace_king_high_is_greater_than_ace_queen_high(self):
        hand1, hand2 = Hand(self.heart_ace_king_high), Hand(self.diamond_ace_queen_high)
        self.assertGreater(hand1, hand2)

    def test_ace_king_high_is_greater_than_ace_six_high(self):
        hand1, hand2 = Hand(self.heart_ace_king_high), Hand(self.ace_6_high)
        self.assertGreater(hand1, hand2)

    def test_ace_six_high_is_greater_than_king_queen_high(self):
        hand1, hand2 = Hand(self.ace_6_high), Hand(self.king_queen_high)
        self.assertGreater(hand1, hand2)

    def test_king_queen_high_is_greater_than_lowest_rank(self):
        hand1, hand2 = Hand(self.king_queen_high), Hand(self.lowest_rank)
        self.assertGreater(hand1, hand2)


if __name__ == '__main__':
    main()
