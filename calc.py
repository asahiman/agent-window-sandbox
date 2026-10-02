def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def avg(values):
    if not values:
        raise ValueError("cannot compute average of empty list")
    return sum(values) / len(values)


def max_of(values):
    if not values:
        raise ValueError("cannot compute max of empty list")
    return max(values)


def median(values):
    if not values:
        raise ValueError("cannot compute median of empty list")
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
