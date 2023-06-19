import unittest


def can_sum(t, nums):

    if t < 0:
        return False
    if t == 0:
        return True

    for n in nums:
        if can_sum(t-n, nums):
            return True
    return False


def can_sum_memo(t, nums, memo=None):
    if memo is None:
        memo = {}
    if t < 0:
        return False
    if t in memo:
        return memo[t]
    if t == 0:
        return True

    for n in nums:
        memo[t-n] = can_sum_memo(t-n, nums, memo)
        if memo[t-n]:
            return True
    return False


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(True, can_sum(7, [5, 3, 4, 7]))
        self.assertEqual(True, can_sum(7, [2, 3]))
        self.assertEqual(False, can_sum(7, [2, 4]))

    def test_02(self):
        self.assertEqual(False, can_sum_memo(300, [7, 14]))


if __name__ == '__main__':
    unittest.main()
