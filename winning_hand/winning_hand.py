from functools import reduce
from operator import eq
from sys import argv

from models.card import Card
from models.hand import Hand


def winning_hand(*inp):
    hands = tuple(Hand(to_cards(hand)) for hand in inp)
    if reduce(eq, hands): return "It's a tie"
    return max(hands)


def to_cards(player_hand):
    return tuple(map(Card, player_hand.split()))


if __name__ == '__main__':
    print(f'The winning hand is --> {winning_hand(*argv[1:])}')
