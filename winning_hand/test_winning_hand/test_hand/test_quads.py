from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestQuads(TestCase):

    def setUp(self) -> None:
        self.triple_ace = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart 2', 'Diamond Q'
        ))
        self.ace_king_full_house = create_mock_cards((
            'Diamond A', 'Club A', 'Spade A', 'Heart K', 'Diamond K'
        ))
        self.quad_king = create_mock_cards((
            'Diamond K', 'Club K', 'Spade K', 'Heart K', 'Diamond 4'
        ))
        self.quad_queen = create_mock_cards((
            'Diamond Q', 'Club Q', 'Spade Q', 'Heart 3', 'Diamond Q'
        ))
        self.quad_3 = create_mock_cards((
            'Diamond 3', 'Club 3', 'Spade 3', 'Heart 3', 'Diamond J'
        ))
        self.quad_2 = create_mock_cards((
            'Diamond 2', 'Club 2', 'Spade 2', 'Heart 12', 'Diamond A'
        ))

    def test_quad_queen_is_greater_than_triple_ace(self):
        hand1, hand2 = Hand(self.quad_queen), Hand(self.triple_ace)
        self.assertGreater(hand1, hand2)

    def test_quad_queen_is_greater_than_ace_king_full_house(self):
        hand1, hand2 = Hand(self.quad_queen), Hand(self.ace_king_full_house)
        self.assertGreater(hand1, hand2)

    def test_quad_king_is_greater_than_quad_queen(self):
        hand1, hand2 = Hand(self.quad_king), Hand(self.quad_queen)
        self.assertGreater(hand1, hand2)

    def test_quad_2_is_less_than_quad_3(self):
        hand1, hand2 = Hand(self.quad_2), Hand(self.quad_3)
        self.assertLess(hand1, hand2)


if __name__ == '__main__':
    main()
