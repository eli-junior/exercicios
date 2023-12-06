import pytest

from day_1.resolution_2 import reverse_word, get_number, NumberNotFound


# def test_parse_number_seventeen():
#     assert parse_numbers('onebhtglzjsmhncmkfln1xj7') == 17


def test_reverse_word_one():
    assert reverse_word('one') == 'eno'


def test_reverse_word_nine():
    assert reverse_word('nine') == 'enin'


def test_get_first_number_one():
    assert get_number('onebhtglzjsmhncmkfln1xj7') == '1'


def test_get_first_number_two():
    assert get_number('two1nine') == '2'


def test_get_first_number_eight():
    assert get_number('eightwothree') == '8'

def test_get_first_number_four():
    assert get_number('4nineeightseven2') == '4'


def test_get_first_number_raises():
    with pytest.raises(NumberNotFound):
        assert get_number('pqrstsi7xteen')


def test_get_second_number_seven():
    assert get_number(reverse_word('onebhtglzjsmhncmkfln1xj7'), reverse=True) == '7'


def test_get_second_number_nine():
    assert get_number(reverse_word('two1nine'), reverse=True) == '9'


def test_get_second_number_three():
    assert get_number(reverse_word('eightwothree'), reverse=True) == '3'


def test_get_second_number_two():
    assert get_number(reverse_word('4nineeightseven2'), reverse=True) == '2'


def test_get_second_number_raises():
    with pytest.raises(NumberNotFound):
        assert get_number('pqrstsiteen', reverse=True)