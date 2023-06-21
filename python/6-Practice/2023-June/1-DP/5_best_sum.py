import unittest


def best_sum(t, nums):
    if t == 0:
        return []
    if t < 0:
        return

    ans = None

    for n in nums:
        v = best_sum(t - n, nums)
        if v is not None:
            v.append(n)
            if ans is None or len(v) < len(ans):
                ans = v

    return ans


def best_sum_memo(t, nums, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == 0:
        return []
    if t < 0:
        return

    ans = None

    for n in nums:
        v = best_sum_memo(t - n, nums, memo)
        if v is not None:
            # v.append(n)
            new_v = v + [n]
            if ans is None or len(new_v) < len(ans):
                ans = new_v

    memo[t] = ans
    return ans


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual([7], best_sum(7, [5, 3, 4, 7]))
        self.assertEqual([5, 3], best_sum(8, [2, 3, 5]))
        self.assertEqual([4, 4], best_sum(8, [1, 4, 5]))

    ''' This will take a very long time '''

    def test_03(self):
        pass
        # self.assertEqual([25, 25, 25, 25], best_sum(100, [1, 2, 5, 25]))      # takes long time

    def test_04(self):
        self.assertEqual([25, 25, 25, 25], best_sum_memo(100, [1, 2, 5, 25]))


if __name__ == '__main__':
    unittest.main()
