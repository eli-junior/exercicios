from calculing_with_func.resolution import *

import pytest

TEST_FINAL_NUMBERS = [
    (zero, "0"),
    (one, "1"),
    (two, "2"),
    (three, "3"),
    (four, "4"),
    (five, "5"),
    (six, "6"),
    (seven, "7"),
    (eight, "8"),
    (nine, "9"),
]

@pytest.mark.parametrize("func, res", TEST_FINAL_NUMBERS)
def test_final_numbers_without_params(func, res):
    assert func() == res
    assert func() == res
    assert func() == res
    assert func() == res
    assert func() == res
    assert func() == res
    assert func() == res
    assert func() == res
    assert func() == res
    assert func() == res


TEST_OPERATORS_AND_NUMBER = [
    (minus, two, "-2"),
    (plus, three, "+3"),
    (times, four, "*4"),
    (divided_by, five, "/5"),

]

@pytest.mark.parametrize("oper, num, res", TEST_OPERATORS_AND_NUMBER)
def test_operators(oper, num, res):
    assert oper(num()) == res
    assert oper(num()) == res
    assert oper(num()) == res
    assert oper(num()) == res


def test_number_four_plus_nine_equals_13():
    assert four(plus(nine())) == 13
def test_number_eight_minus_three_equals_5():
    assert eight(minus(three())) == 5
def test_number_six_divided_by_two_equals_3():
    assert six(divided_by(two())) == 3
def test_number_seven_times_five_equals_35():
    assert seven(times(five())) == 35
