import unittest


def ans1(nums, k):
    memo = {}
    print('\nidx, i, t, max_value, memo')
    return dpmemo(nums, k, 0, nums[0], memo)
    # return dp(nums, k, 0, nums[0])


def dpmemo(nums, k, idx, t, memo):
    # print(k, idx, t)
    if idx in memo:
        # return memo[idx] + nums[idx]
        return t + memo[idx]
        # return t + nums[idx]
    if idx == len(nums) - 1:
        return t

    i = idx + 1
    p = []

    while i < len(nums) and i <= idx + k:
        max_value = dpmemo(nums, k, i, t + nums[i], memo)
        print(idx, i, t, max_value, memo)
        p.append(max_value)
        i += 1

    m = max(p)
    if idx in memo:
        # memo[idx] = max(memo[idx], m - t + nums[idx])
        memo[idx] = max(memo[idx], m - t)
        # memo[idx] = max(memo[idx], m)
    else:
        # memo[idx] = m - t + nums[idx]
        memo[idx] = m - t
        # memo[idx] = m

    return m


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(17, ans1([10, -5, -2, 4, 0, 3], 3))
        self.assertEqual(0, ans1([1,-5,-20,4,-1,3,-6,-3], 2))
        self.assertEqual(7, ans1([1,-1,-2,4,-7,3], 2))


if __name__ == '__main__':
    unittest.main()
