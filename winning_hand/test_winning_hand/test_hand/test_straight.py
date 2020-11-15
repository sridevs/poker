from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestStraight(TestCase):

    def setUp(self) -> None:
        self.triple_ace = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart K', 'Diamond Q'
        ))
        self.wheel = create_mock_cards((
            'Diamond A', 'Club 2', 'Spade 3', 'Heart 4', 'Diamond 5'
        ))
        self.six_straight = create_mock_cards((
            'Diamond 2', 'Club 3', 'Spade 4', 'Heart 5', 'Diamond 6'
        ))
        self.king_straight = create_mock_cards((
            'Diamond K', 'Club Q', 'Spade J', 'Heart 10', 'Diamond 9'
        ))
        self.broadway = create_mock_cards((
            'Diamond A', 'Club K', 'Spade Q', 'Heart J', 'Diamond 10'
        ))

    def test_wheel_is_greater_than_triple_ace(self):
        hand1, hand2 = Hand(self.wheel), Hand(self.triple_ace)
        self.assertGreater(hand1, hand2)

    def test_six_straight_is_greater_than_wheel(self):
        hand1, hand2 = Hand(self.six_straight), Hand(self.wheel)
        self.assertGreater(hand1, hand2)

    def test_king_straight_is_greater_than_six_straight(self):
        hand1, hand2 = Hand(self.king_straight), Hand(self.six_straight)
        self.assertGreater(hand1, hand2)

    def test_king_straight_is_less_than_broadway(self):
        hand1, hand2 = Hand(self.king_straight), Hand(self.broadway)
        self.assertLess(hand1, hand2)

    def test_king_straight_is_greater_than_triple_ace(self):
        hand1, hand2 = Hand(self.king_straight), Hand(self.triple_ace)
        self.assertGreater(hand1,hand2)


if __name__ == '__main__':
    main()
