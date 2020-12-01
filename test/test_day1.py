from pytest import fixture

from adventOfCode import day1


@fixture
def data():
    return [2, 3, 1, 8, 1, 4, 3]


def test_ex1(data):
    res = day1.ex1(data, 7)
    assert res == 4 * 3


def test_ex2(data):
    res = day1.ex2(data, 7)
    assert res == 2 * 4 * 1
