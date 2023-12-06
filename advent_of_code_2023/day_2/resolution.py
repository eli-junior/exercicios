MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def load_lines(path: str):
    with open(path, "r") as file:
        return file.readlines()


def round_interface(red=0, green=0, blue=0):
    return dict(
        red=red,
        green=green,
        blue=blue
    )


def get_game_number(line: str):
    number, rounds = line.split(':')
    return int(number.split(' ')[-1]), rounds.strip()


def parse_rounds(rounds: str):
    rounds = [r.strip() for r in rounds.split(';')]
    round_list = []
    for round in rounds:
    
        dict_colors = {}
        for colors in round.split(','):
            colors = colors.strip()
            q, c = colors.split(' ')
            dict_colors[c] = int(q)
        round_list.append(round_interface(**dict_colors))
    return round_list


def parse_game(line: str):
    game_number, rounds = get_game_number(line)        
    return {game_number: parse_rounds(rounds)}


def validate(game: dict[int, list[str, int]]) -> bool:
    rounds = list(game.values())[0]
    for r in rounds:
        if valid := all((r[c] <= MAX_CUBES[c] for c in r.keys())):
            continue
        return False
    return valid


def set_power(game):
    red = 1
    green = 1
    blue = 1
    for g in game:
        red = g['red'] if g['red'] > red else red
        green = g['green'] if g['green'] > green else green
        blue = g['blue'] if g['blue'] > blue else blue
    return red * green * blue


def part_one():
    path = './input.txt'
    valids = {}
    for line in load_lines(path):
        game = parse_game(line)
        if validate(game):
            valids.update(game)
    print(sum(list(valids.keys())))


def part_two():
    path = './input.txt'
    total = 0

    for line in load_lines(path):
        game = parse_game(line)
        for v in game.values():
            total += set_power(v)
    print(total)


if __name__ == '__main__':
    # part_one()  	
    part_two()