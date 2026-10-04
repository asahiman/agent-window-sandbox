def add(a, b):
    """Return the sum of a and b."""
    return a + b


def sub(a, b):
    """Return the difference of a and b (a - b)."""
    return a - b


def mul(a, b):
    """Return the product of a and b."""
    return a * b


def div(a, b):
    """Return a divided by b, raising ValueError if b is zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def avg(values):
    """Return the arithmetic mean of values, raising ValueError if empty."""
    if not values:
        raise ValueError("cannot compute average of empty list")
    return sum(values) / len(values)


def max_of(values):
    """Return the largest item in values, raising ValueError if empty."""
    if not values:
        raise ValueError("cannot compute max of empty list")
    return max(values)


def median(values):
    """Return the median of values, raising ValueError if empty."""
    if not values:
        raise ValueError("cannot compute median of empty list")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
