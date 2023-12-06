from collections import namedtuple
from itertools import combinations

SYMBOLS = r"/*=+%'}#,${@&-"

Point = namedtuple('Point', ['x', 'y'])
Number = namedtuple('Number', ['line', 'start', 'stop'])


def find_symbols(matrix, symbols=SYMBOLS):
    found_symbols = []
    for i, mat in enumerate(matrix):
        for j, pos in enumerate(mat):
            if pos in symbols:
                found_symbols.append(Point(i, j))
    return tuple(found_symbols)



def make_matrix(_input: str):
    _input = _input.strip().split('\n')
    return [x.strip() for x in _input]


def find_numbers(matrix, points: list[Point]):
    possibilities = ((+1, +1), (-1, +1), (+1, -1), (-1, -1), (0, -1), (0, +1), (+1, 0), (-1, 0))
    numbers = []
    for point in points:
        for pos in possibilities:
            np = Point((point.x + pos[0]), (point.y + pos[1]))
            if np.x < 0:
                continue
            try:
                char = matrix[np.x][np.y]
            except IndexError:
                continue
            else:
                if not char.isnumeric():
                    continue
            line = np.x
            start, stop = np.y, np.y
            try:
                while char.isnumeric():
                    char = matrix[line][(start - 1)]
                    if char.isnumeric():
                        start -= 1

            except IndexError:
                pass
            
            char = matrix[line][stop]
            try:
                while char.isnumeric():
                    stop += 1
                    char = matrix[line][stop]

            except IndexError:
                pass

            numbers.append(Number(line, start, stop))
    return list(set(numbers))


def find_numbers_only_gears(matrix, points: list[Point]):
    possibilities = ((+1, +1), (-1, +1), (+1, -1), (-1, -1), (0, -1), (0, +1), (+1, 0), (-1, 0))
    numbers = []
    for point in points:
        pairs = []
        for pos in possibilities:
            np = Point((point.x + pos[0]), (point.y + pos[1]))
            if np.x < 0:
                continue
            try:
                char = matrix[np.x][np.y]
            except IndexError:
                continue
            else:
                if not char.isnumeric():
                    continue
            line = np.x
            start, stop = np.y, np.y
            try:
                while char.isnumeric():
                    char = matrix[line][(start - 1)]
                    if char.isnumeric():
                        start -= 1

            except IndexError:
                pass
            
            char = matrix[line][stop]
            try:
                while char.isnumeric():
                    stop += 1
                    char = matrix[line][stop]

            except IndexError:
                pass
            pairs.append(Number(line, start, stop))
        if len(pairs) > 1:
            numbers.append(tuple(set(pairs)))
    return list(set(numbers))


def part_one(file=None):
    if not file:
        with open('./input.txt', 'r') as f:
            file = f.read()
    matrix = make_matrix(file)
    all_symbol_points = find_symbols(matrix)
    all_numbers = find_numbers(matrix, all_symbol_points)
    numbers = []
    result = 0
    for n in all_numbers:
        number = int(matrix[n.line][n.start:n.stop])
        numbers.append(number)
        result += number

    print(sorted(numbers))
    print(result)
    return result

def part_two(file=None):
    if not file:
        with open('./input.txt', 'r') as f:
            file = f.read()
    matrix = make_matrix(file)
    all_symbol_points = find_symbols(matrix, symbols='*')
    all_numbers = find_numbers_only_gears(matrix, all_symbol_points)
    result = 0
    for number in all_numbers:
        partial = 1
        if len(number) == 1:
            continue
        for n in number:
            partial *= int(matrix[n.line][n.start:n.stop])
        # print(partial)
        result += partial
    print(result)
    return
    numbers = []
    result = 0
    for n in all_numbers:
        number = int(matrix[n.line][n.start:n.stop])
        numbers.append(number)
        result += number

    print(sorted(numbers))
    print(result)
    return result


if __name__ == '__main__':
    # part_one()
    part_two()
