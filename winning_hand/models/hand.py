from models.check_rank import is_straight, is_wheel, is_flush, has_two_pair, is_full_house
from models.rank_value import RankValue


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return f'{self.cards}'

    def __eq__(self, other):
        return isinstance(other, Hand) and self.value() == other.value()

    def __gt__(self, other):
        return isinstance(other, Hand) and self.value() > other.value()

    @staticmethod
    def update_pair_count_and_hand_value(hand_value, pair_counts):
        pair_value = []
        for card_value in set(hand_value):
            pair_count = hand_value.count(card_value) / 2
            if pair_count >= 1:
                pair_counts.append(pair_count)
                pair_value.insert(0, RankValue.pair_multiplier ** pair_count * card_value)
        hand_value.extend(pair_value)
        hand_value.sort(reverse=True)

    def value(self):
        hand_value, hand_suite, pair_counts = [], [], []
        straight, flush = False, False
        for card in self.cards:
            hand_value.append(card.value())
            hand_suite.append(card.suite())
        self.update_pair_count_and_hand_value(hand_value, pair_counts)

        # Two pair
        if has_two_pair(pair_counts):
            hand_value.insert(0, RankValue.double)
            # Full house
            if is_full_house(pair_counts):
                hand_value.insert(0, RankValue.full_house)

        # Straight
        elif is_straight(hand_value):
            straight = True
            hand_value.insert(0, RankValue.straight)

        # Wheel
        elif is_wheel(hand_value):
            straight = True
            hand_value.insert(0, RankValue.wheel)

        # Flush
        if is_flush(hand_suite):
            flush = True
            hand_value.insert(0, RankValue.flush)

        # Straight Flush
        if straight and flush:
            hand_value.insert(0, RankValue.straight_flush)

        return sorted(hand_value, reverse=True)
