import pytest

from main import flatten


def test_flatten():
    assert flatten


def test_flatten_sending_only_single_elements():
    assert flatten(1, 2, 3, None, "oi") == [1, 2, 3, None, "oi"]


def test_flatten_with_one_level_deph():
    assert flatten(1, [2, 3], 4, 5, [6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_flatten_with_more_levels():
    assert flatten('a', ['b', 2], 3, None, [[4], ['c']]) == ['a', 'b', 2, 3, None, 4, 'c']
