from day_2.resolution import parse_game, round_interface, get_game_number, parse_rounds, set_power


def test_parse_rounds_game_one():
    expected = [{'red': 4, 'green': 0, 'blue': 3}, {'red': 1, 'green': 2, 'blue': 6}, {'red': 0, 'green': 2, 'blue': 0}]
    assert parse_rounds('3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == expected


def test_get_game_number_one():
    assert get_game_number('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == (1, '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') 


def test_game_round_complete_interface():
    assert round_interface(green=1, blue=100, red=30) == {
        'red': 30,
        'green': 1,
        'blue': 100
    }

def test_game_round_without_red():
    assert round_interface(green=1, blue=100) == {
        'red': 0,
        'green': 1,
        'blue': 100
    }

def test_game_round_without_blue():
    assert round_interface(green=1, red=100) == {
        'red': 100,
        'green': 1,
        'blue': 0
    }


def test_parse_input_game_one():
    expected = {
        1: [
            {
                'red': 4,
                'green': 0,
                'blue': 3,
            },
            {
                'red': 1,
                'green': 2,
                'blue': 6,

            },
            {
                'red': 0,
                'green': 2,
                'blue': 0,
            }
        ]
    }
    assert parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == expected


def test_parse_input_game_two():
    expected = {
        2: [
            {
                'red': 0,
                'green': 2,
                'blue': 1,
            },
            {
                'red': 1,
                'green': 3,
                'blue': 4,

            },
            {
                'red': 0,
                'green': 1,
                'blue': 1,
            }
        ]
    }
    assert parse_game('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == expected


def test_parse_input_game_twenty():
    expected = {
        20: [
            {
                'red': 0,
                'green': 2,
                'blue': 1,
            },
            {
                'red': 1,
                'green': 3,
                'blue': 4,

            },
            {
                'red': 0,
                'green': 1,
                'blue': 1,
            }
        ]
    }
    assert parse_game('Game 20: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == expected


def test_set_minimum():
    game = [
        {'red': 0, 'green': 9, 'blue': 7},
        {'red': 3, 'green': 1, 'blue': 4},
        {'red': 15, 'green': 9, 'blue': 0},
        {'red': 6, 'green': 13, 'blue': 3},
        {'red': 2, 'green': 12, 'blue': 11}]
    assert set_power(game) ==  15 * 13 * 11
                                                                                                                                          