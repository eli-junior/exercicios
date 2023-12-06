from day_3.resolution import make_matrix, find_symbols, find_numbers, part_one, Point, Number


def test_schematic_success():
    _input = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598.."""

    assert part_one(_input) == 4361

def test_make_matrix():
    _input = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598.."""
    expected = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..',
    ]
    assert make_matrix(_input) == expected


def test_point():
    p = Point(1, 30)
    assert p.x == 1 and p.y == 30


def test_number():
    n = Number(1, 0, 30)
    assert n.line ==1 and n.start == 0 and n.stop == 30

def test_find_symbols():
    matrix = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
    ]
    a = Point(1, 3)
    b = Point(3, 6)
    assert find_symbols(matrix) == ((a, b))


def test_find_numbers_one_valid():
    matrix = [
        '467..114..',
        '...*......',
    ]
    points = find_symbols(matrix)
    assert find_numbers(matrix, points) == [Number(0, 0, 3)]


def test_find_numbers_three_valids():
    matrix = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
    ]
    points = find_symbols(matrix)
    assert find_numbers(matrix, points) == [Number(2, 2, 4), Number(2, 6, 9), Number(0, 0, 3)]


def test_find_numbers_three_problematic():
    matrix = [
        '......#...',
        '617*......',
        '.....+.58.',
    ]
    points = find_symbols(matrix)
    assert find_numbers(matrix, points) == [Number(line=1, start=0, stop=3)]


def test_find_numbers_three_valids_with_shadow():
    matrix = [
        '467..114..',
        '$..*......',
        '..35..633.',
        '......#...',
    ]
    points = find_symbols(matrix)
    assert find_numbers(matrix, points) == [Number(2, 2, 4), Number(2, 6, 9), Number(0, 0, 3)]