import unittest


def how_sum(t, nums):
    if t == 0:
        return []
    if t < 0:
        return

    for n in nums:
        v = how_sum(t-n, nums)
        if v is not None:
            v.append(n)
            return v

    return


def how_sum_memo(t, nums, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == 0:
        return []
    if t < 0:
        return

    for n in nums:
        v = how_sum_memo(t-n, nums, memo)
        memo[t-n] = v
        if v is not None:
            v.append(n)
            return v

    return


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual([4, 3], how_sum(7, [5, 3, 4, 7]))
        self.assertEqual([3, 2, 2], how_sum(7, [2, 3]))
        self.assertEqual([3, 2], how_sum(5, [2, 3]))
        self.assertEqual(None, how_sum(7, [2, 4]))
        # print(how_sum(5, [2, 3]))

    def test_02(self):
        self.assertEqual([4, 3], how_sum_memo(7, [5, 3, 4, 7]))
        self.assertEqual([3, 2, 2], how_sum_memo(7, [2, 3]))
        self.assertEqual([4, 3], how_sum_memo(7, [5, 3, 4, 7]))
        self.assertEqual(None, how_sum_memo(7, [2, 4]))
        self.assertEqual([3, 2], how_sum_memo(5, [2, 3]))

        print(how_sum_memo(7, [2, 4]))

    def test_03(self):
        self.assertEqual(None, how_sum_memo(300, [7, 14]))
        self.assertEqual([100, 100, 100], how_sum_memo(300, [100, 7, 14]))

    def test_04(self):
        self.assertEqual([3, 2, 2], how_sum_memo(7, [2, 3]))


if __name__ == '__main__':
    unittest.main()
