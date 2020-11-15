def is_straight(values):
    diff = []
    for pos in range(len(values[:-1])):
        diff.append(values[pos] - values[pos + 1])
    return set(diff) == {1}


def is_wheel(values):
    return set(values) == {14, 5, 4, 3, 2}


def is_flush(hand_suite):
    return len(set(hand_suite)) == 1


def has_two_pair(pairs_count):
    return len(pairs_count) > 1


def is_full_house(pairs_count):
    return sum(pairs_count) > 2