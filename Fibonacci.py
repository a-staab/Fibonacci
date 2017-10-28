import unittest


def memo(function):
    """Returns a memoized version of single-argument function."""

    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = function(n)
        return cache[n]
    return memoized


@memo
def fib(n):
    """Returns the nth term of the Fibonacci sequence."""

    # Check for valid input
    if not n >= 0:
        raise ValueError("'n' must be greater than or equal to 0.")

    # Recursively compute value
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


class FibonacciTestCase(unittest.TestCase):

    def test_first_base_case(self):
        assert fib(0) == 0

    def test_second_base_case(self):
        assert fib(1) == 1

    def test_small_n(self):
        assert fib(4) == 3

    def test_large_n(self):
        assert fib(200) == 280571172992510140037611932413038677189525


# Uncomment below to test

# if __name__ == "__main__":
#     unittest.main()
