import unittest


def fib_recur(n):
    if n <= 2:
        return 1
    ans = fib_recur(n - 1) + fib_recur(n - 2)
    return ans


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    ans = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = ans
    return ans


def fib_tab(n):
    tab = [1] * n
    if n > 1:
        tab[0] = 1
    if n > 2:
        tab[1] = 1
    i = 2
    while i < n:
        tab[i] = tab[i - 1] + tab[i - 2]
        i += 1

    return tab[n - 1]


fib = [1, 2, 3, 4, 5, 6, 7, 20, 30, 40, 50]
fib_dict = {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    6: 8,
    7: 13,
    8: 21,
    9: 34,
    20: 6765,
    30: 832040,
    40: 102334155,
    50: 12586269025
}


class MyTestCase(unittest.TestCase):

    def test_1(self):
        for i in range(len(fib)):
            n = fib[i]
            if n <= 20:
                self.assertEqual(fib_recur(n), fib_dict[n])

    def test_2(self):
        for i in range(len(fib)):
            n = fib[i]
            self.assertEqual(fib_memo(n), fib_dict[n])

    def test_3(self):
        for i in range(len(fib)):
            n = fib[i]
            self.assertEqual(fib_tab(n), fib_dict[n])


if __name__ == '__main__':
    unittest.main()
