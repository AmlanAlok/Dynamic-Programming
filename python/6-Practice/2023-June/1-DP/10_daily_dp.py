import unittest

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


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def grid_traveler_memo(m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[(m, n)] = grid_traveler_memo(m - 1, n, memo) + grid_traveler_memo(m, n - 1, memo)
    return memo[(m, n)]


def can_sum_memo(t, nums, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == 0:
        return True
    if t < 0:
        return False

    for n in nums:
        if can_sum_memo(t - n, nums, memo):
            memo[t - n] = True
            return True
    memo[t] = False
    return False


class MyTestCase(unittest.TestCase):

    def test_1(self):
        for i in range(len(fib)):
            n = fib[i]
            self.assertEqual(fib_memo(n), fib_dict[n])

    def test_2(self):
        self.assertEqual(3, grid_traveler_memo(2, 3))
        self.assertEqual(6, grid_traveler_memo(3, 3))
        self.assertEqual(35345263800, grid_traveler_memo(20, 20))

    def test_3(self):
        self.assertEqual(True, can_sum_memo(7, [5, 3, 4, 7]))
        self.assertEqual(True, can_sum_memo(7, [2, 3]))
        self.assertEqual(False, can_sum_memo(7, [2, 4]))
        self.assertEqual(False, can_sum_memo(300, [7, 14]))


if __name__ == '__main__':
    unittest.main()
