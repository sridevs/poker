from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestThreeOfAKind(TestCase):

    def setUp(self) -> None:
        self.two_pair_A_and_K = create_mock_cards((
            'Diamond A', 'Club A', 'Spade K', 'Heart K', 'Diamond Q'
        ))
        self.triple_ace = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart 2', 'Diamond Q'
        ))
        self.triple_king = create_mock_cards((
            'Diamond K', 'Club K', 'Spade K', 'Heart Q', 'Diamond J'
        ))
        self.triple_2 = create_mock_cards((
            'Diamond 2', 'Club 2', 'Spade 2', 'Heart 10', 'Diamond 8'
        ))
        self.triple_2_ace_high = create_mock_cards((
            'Diamond 2', 'Club 2', 'Spade 2', 'Heart A', 'Diamond Q'
        ))
        self.triple_3 = create_mock_cards((
            'Diamond 3', 'Club 3', 'Spade 3', 'Heart 5', 'Diamond 4'
        ))

    def test_triple_ace_is_greater_than_two_pair_A_and_K(self):
        hand1, hand2 = Hand(self.triple_ace), Hand(self.two_pair_A_and_K)
        self.assertGreater(hand1, hand2)

    def test_triple_ace_is_greater_than_triple_K(self):
        hand1, hand2 = Hand(self.triple_ace), Hand(self.triple_king)
        self.assertGreater(hand1, hand2)

    def test_triple_2_ace_high_is_greater_than_than_triple_2(self):
        hand1, hand2 = Hand(self.triple_2_ace_high), Hand(self.triple_2)
        self.assertGreater(hand1, hand2)

    def test_triple_2_ace_high_is_lower_than_triple_3(self):
        hand1, hand2 = Hand(self.triple_2_ace_high), Hand(self.triple_3)
        self.assertLess(hand1, hand2)


if __name__ == '__main__':
    main()
