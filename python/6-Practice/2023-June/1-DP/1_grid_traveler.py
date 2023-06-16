import unittest


def grid_traveler(m, n):
    if m == 0 or n == 0:
        return 0
    if (m, n) == (1, 1):
        return 1

    ans = grid_traveler(m - 1, n) + grid_traveler(m, n - 1)
    return ans


def grid_traveler_memo(m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if (m, n) == (1, 1):
        return 1

    memo[(m, n)] = grid_traveler_memo(m - 1, n, memo) + grid_traveler_memo(m, n - 1, memo)
    return memo[(m, n)]


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(3, grid_traveler(2, 3))
        self.assertEqual(6, grid_traveler(3, 3))

    def test_02(self):
        self.assertEqual(3, grid_traveler_memo(2, 3))
        self.assertEqual(6, grid_traveler_memo(3, 3))
        self.assertEqual(35345263800, grid_traveler_memo(20, 20))


if __name__ == '__main__':
    unittest.main()
