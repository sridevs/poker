from unittest import mock

from models.card import Card

special_card_value = {
    'j': 11,
    'q': 12,
    'k': 13,
    'a': 14
}


def create_mock_card(card):
    mock_card = mock.Mock(spec=Card)
    card_suite, card_value = tuple(card.lower().split())
    mock_card.value.return_value = special_card_value.get(card_value) or int(card_value)
    mock_card.suite.return_value = card_suite
    mock_card.__repr__ = lambda _: card
    mock_card.__gt__ = lambda self, other: self.value() > other.value()
    return mock_card


def create_mock_cards(cards):
    return tuple(map(create_mock_card, cards))
