import calc


def test_add():
    assert calc.add(1, 2) == 3


def test_sub():
    assert calc.sub(3, 1) == 2


def test_mul():
    assert calc.mul(3, 4) == 12
