class Card:
    special_card_value = {
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    suite_name = {
        'S': 'Spade',
        'H': 'Heart',
        'D': 'Diamond',
        'C': 'Club'
    }

    def __init__(self, card_details):
        self._name = card_details[:-1].upper()
        self._suite = card_details[-1:].upper()

    def value(self):
        return Card.special_card_value.get(self._name) or int(self._name)

    def suite(self):
        return self._suite

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Card) and self.value() == o.value()

    def __lt__(self, other):
        return self.value() < other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __repr__(self):
        return f'{Card.suite_name[self._suite]} {self._name}'
