import unittest


def fib(n):

    if n <= 2:
        return 1

    return fib(n-1) + fib(n-2)


class MyTestCase(unittest.TestCase):

    def test_something(self):

        self.assertEqual(8, fib(6))
        self.assertEqual(13, fib(7))


if __name__ == '__main__':
    unittest.main()
