from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestFullHouse(TestCase):

    def setUp(self) -> None:
        self.triple_ace = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart 2', 'Diamond Q'
        ))
        self.ace_full_house = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart 2', 'Diamond 2'
        ))
        self.K_Q_full_house = create_mock_cards((
            'Diamond K', 'Club K', 'Spade K', 'Heart Q', 'Diamond Q'
        ))
        self.triple_2_10_full_house = create_mock_cards((
            'Diamond 2', 'Club 2', 'Spade 2', 'Heart 10', 'Diamond 10'
        ))
        self.triple_3_4_full_house = create_mock_cards((
            'Diamond 3', 'Club 3', 'Spade 3', 'Heart 4', 'Diamond 4'
        ))
        self.flush = create_mock_cards((
            'Diamond A', 'Diamond K', 'Diamond Q', 'Diamond J', 'Diamond 9'
        ))
        self.straight = create_mock_cards((
            'Diamond 10', 'Club J', 'Spade Q', 'Heart K', 'Diamond A'
        ))

    def test_K_Q_full_house_is_greater_than_triple_ace(self):
        hand1, hand2 = Hand(self.K_Q_full_house), Hand(self.triple_ace)
        self.assertGreater(hand1, hand2)

    def test_K_Q_full_house_is_less_than_ace_full_house(self):
        hand1, hand2 = Hand(self.K_Q_full_house), Hand(self.ace_full_house)
        self.assertLess(hand1, hand2)

    def test_triple_2_10_full_house_is_greater_than_triple_ace(self):
        hand1, hand2 = Hand(self.triple_2_10_full_house), Hand(self.triple_ace)
        self.assertGreater(hand1, hand2)

    def test_triple_2_10_full_house_is_less_than_3_4_full_house(self):
        hand1, hand2 = Hand(self.triple_2_10_full_house), Hand(self.triple_3_4_full_house)
        self.assertLess(hand1, hand2)

    def test_flush_is_less_than_full_house(self):
        hand1, hand2 = Hand(self.flush), Hand(self.triple_2_10_full_house)
        self.assertLess(hand1, hand2)

    def test_straight_is_less_than_full_house(self):
        hand1, hand2 = Hand(self.straight), Hand(self.triple_2_10_full_house)
        self.assertLess(hand1, hand2)


if __name__ == '__main__':
    main()
