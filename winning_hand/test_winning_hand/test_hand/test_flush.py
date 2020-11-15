from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestFlush(TestCase):

    def setUp(self) -> None:
        self.triple_ace = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart K', 'Diamond Q'
        ))
        self.wheel = create_mock_cards((
            'Diamond A', 'Club 2', 'Spade 3', 'Heart 4', 'Diamond 5'
        ))
        self.ace_flush = create_mock_cards((
            'Heart A', 'Heart K', 'Heart Q', 'Heart J', 'Heart 9'
        ))
        self.low_flush = create_mock_cards((
            'Club 2', 'Club 3', 'Club 4', 'Club 5', 'Club 7'
        ))
        self.broadway = create_mock_cards((
            'Diamond A', 'Club K', 'Spade Q', 'Heart J', 'Diamond 10'
        ))

    def test_low_flush_is_greater_than_triple_ace(self):
        hand1, hand2 = Hand(self.low_flush), Hand(self.triple_ace)
        self.assertGreater(hand1, hand2)

    def test_low_flush_is_greater_than_wheel(self):
        hand1, hand2 = Hand(self.low_flush), Hand(self.wheel)
        self.assertGreater(hand1, hand2)

    def test_low_flush_is_greater_than_broadway(self):
        hand1, hand2 = Hand(self.low_flush), Hand(self.broadway)
        self.assertGreater(hand1, hand2)

    def test_low_flush_is_less_than_ace_flush(self):
        hand1, hand2 = Hand(self.low_flush), Hand(self.ace_flush)
        self.assertLess(hand1, hand2)


if __name__ == '__main__':
    main()
