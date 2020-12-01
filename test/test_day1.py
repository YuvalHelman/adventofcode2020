from pytest import fixture

from adventOfCode import day1


@fixture
def data():
    return [2, 3, 1, 8, 1, 4]


def test_ex1():
    res = day1.ex1(data, 7)
    assert res == 12
