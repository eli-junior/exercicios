from collections import namedtuple

Cards = namedtuple('Cards', ['winning', 'mine'])

def clean(list_numbers: str) -> tuple[int]:
    numbers = list_numbers.strip().split(" ")
    cleaned = []
    for n in numbers:
        cleaned.append(int(n)) if n else None
    return tuple(cleaned)


def separate_numbers(card):
    card = card.split(':')[-1]
    winning, mine = card.split('|')
    winning = clean(winning)
    mine = clean(mine)
    return Cards(winning, mine)

def card_points(card):
    mutiply = 2
    cards = Cards(*separate_numbers(card))
    return len(set(cards.winning).intersection(cards.mine))


def points_calculator(total: int) -> int:
    match total:
        case 0:
            response = 0
        case 1:
            response = 1
        case 2:
            response = 2
        case _:
            response = 1
            for _ in range(total -1):
                response *= 2
    return response

def part_one():
    with open('./input.txt', 'r') as f:
        cards = f.readlines()
    total = 0

    for c in cards:
        points = card_points(c)
        total += points_calculator(points)
        print(total)


def part_two(cards=None):
    if not cards:
        with open('./input.txt', 'r') as f:
            cards = f.readlines()
    
    total = 0
    while cards:
        c = cards.pop(0)
        points = card_points(c)
    
        total += 1
        print(total)
        shadow = cards[:points].copy()
        cards.extend(shadow)
        print(cards)
        if total == 2:
            break
    print(total)
    return total

if __name__ == '__main__':
    # part_one()
    part_two()
