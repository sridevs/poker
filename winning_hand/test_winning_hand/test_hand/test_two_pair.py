from unittest import TestCase, main

from models.hand import Hand
from test_winning_hand.mock_card import create_mock_cards


class TestTwoPair(TestCase):

    def setUp(self) -> None:
        self.double_ace = create_mock_cards((
            'Club A', 'Spade 2', 'Diamond J', 'Diamond 4', 'Heart A'
        ))
        self.two_pair_2_and_5 = create_mock_cards((
            'Diamond 3', 'Club 5', 'Spade 5', 'Heart 2', 'Diamond 2'
        ))
        self.two_pair_2_and_5_ace_high = create_mock_cards((
            'Diamond A', 'Club 5', 'Spade 5', 'Heart 2', 'Diamond 2'
        ))
        self.two_pair_10_and_8 = create_mock_cards((
            'Diamond K', 'Club 8', 'Spade 10', 'Heart 10', 'Diamond 8'
        ))
        self.two_pair_J_and_2 = create_mock_cards((
            'Diamond 2', 'Club 2', 'Spade J', 'Heart J', 'Diamond 3'
        ))
        self.two_pair_A_and_K = create_mock_cards((
            'Diamond A', 'Club A', 'Spade K', 'Heart K', 'Diamond 7'
        ))
        self.two_pair_2_and_3 = create_mock_cards((
            'Diamond 2', 'Club 2', 'Spade 3', 'Heart 5', 'Diamond 3'
        ))
        self.two_pair_2_and_3_similar = create_mock_cards((
            'Heart 2', 'Diamond 3', 'Heart 3', 'Spade 2', 'Spade 5'
        ))

    def test_two_pair_2_and_5_is_greater_than_double_ace(self):
        hand1, hand2 = Hand(self.two_pair_2_and_5), Hand(self.double_ace)
        self.assertGreater(hand1, hand2)

    def test_two_pair_2_and_5_ace_high_is_greater_than_two_pair_2_and_5(self):
        hand1, hand2 = Hand(self.two_pair_2_and_5_ace_high), Hand(self.two_pair_2_and_5)
        self.assertGreater(hand1, hand2)

    def test_equality_of_similar_two_pair_2_and_3(self):
        hand1, hand2 = Hand(self.two_pair_2_and_3), Hand(self.two_pair_2_and_3_similar)
        self.assertEqual(hand1, hand2)

    def test_two_pair_J_and_2_is_greater_than_two_pair_10_and_8(self):
        hand1, hand2 = Hand(self.two_pair_J_and_2), Hand(self.two_pair_10_and_8)
        self.assertGreater(hand1, hand2)

    def test_two_pair_A_and_K_is_greater_than_two_pair_J_and_2(self):
        hand1, hand2 = Hand(self.two_pair_A_and_K), Hand(self.two_pair_J_and_2)
        self.assertGreater(hand1, hand2)

    def test_two_pair_2_and_3_is_greater_than_double_ace(self):
        hand1, hand2 = Hand(self.two_pair_2_and_3), Hand(self.double_ace)
        self.assertGreater(hand1, hand2)

    def test_two_pair_2_and_3_is_lower_than_2_and_5(self):
        hand1, hand2 = Hand(self.two_pair_2_and_3), Hand(self.two_pair_2_and_5)
        self.assertLess(hand1, hand2)


if __name__ == '__main__':
    main()
