import pytest

import calc


def test_add():
    assert calc.add(1, 2) == 3


def test_sub():
    assert calc.sub(3, 1) == 2


def test_mul():
    assert calc.mul(3, 4) == 12


def test_div():
    assert calc.div(6, 3) == 2
    assert calc.div(1, 2) == 0.5


def test_div_by_zero():
    with pytest.raises(ValueError):
        calc.div(1, 0)


def test_max_of_multiple():
    assert calc.max_of([1, 5, 3]) == 5


def test_max_of_single():
    assert calc.max_of([7]) == 7


def test_max_of_negatives():
    assert calc.max_of([-5, -2, -9]) == -2


def test_max_of_empty():
    with pytest.raises(ValueError):
        calc.max_of([])


def test_median_odd():
    assert calc.median([3, 1, 2]) == 2


def test_median_even():
    assert calc.median([4, 1, 3, 2]) == 2.5


def test_median_empty():
    with pytest.raises(ValueError):
        calc.median([])
