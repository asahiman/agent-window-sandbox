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
