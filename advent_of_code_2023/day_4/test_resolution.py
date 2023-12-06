from day_4.resolution import card_points, separate_numbers, points_calculator, part_two


def test_card_one_separate_numbers():
    card = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
    winning = (41, 48, 83, 86, 17)
    mine = (83, 86, 6, 31, 17, 9, 48, 53)
    assert separate_numbers(card) == (winning, mine)

def test_card_one():
    card = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
    points = 8
    assert points_calculator(card_points(card)) == points


def test_card_two():
    card = 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'
    points = 2
    assert points_calculator(card_points(card)) == points


def test_card_three():
    card = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'
    points = 2
    assert points_calculator(card_points(card)) == points


def test_card_four():
    card = 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'
    points = 1
    assert points_calculator(card_points(card)) == points

def test_card_five():
    card = 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'
    points = 0
    assert points_calculator(card_points(card)) == points

def test_card_six():
    card = 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
    points = 0
    assert points_calculator(card_points(card)) == points

def test_copy_cards():
    cards = [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
    ]
    assert part_two(cards) == 30
