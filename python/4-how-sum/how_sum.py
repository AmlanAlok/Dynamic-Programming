import unittest


def how_sum(target_sum, numbers):

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for n in numbers:
        remainder = target_sum - n
        # ans.append(n)

        ans = how_sum(remainder, numbers)
        if ans is not None:
            return ans + [n]                # ans.append(n) returns None

    return ans


def how_sum_memo(target_sum, numbers, memo={}, ans=[]):

    # if target_sum in memo:
    #     return memo[target_sum]
    # if target_sum == 0:
    #     return True, ans
    # if target_sum < 0:
    #     return False, ans
    #
    # for n in numbers:
    #     remainder = target_sum - n
    #     ans.append(n)
    #
    #     memo[remainder] = how_sum_memo(remainder, numbers, memo, ans)
    #     if memo[remainder]:
    #         return True
    # return False

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for n in numbers:
        remainder = target_sum - n
        # ans.append(n)

        ans = how_sum(remainder, numbers)
        if ans is not None:
            return ans + [n]                # ans.append(n) returns None

    return ans




class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual([4, 3], how_sum(7, [5, 3, 4, 7]))
        self.assertEqual([3, 2, 2], how_sum(7, [2, 3]))
        self.assertEqual([3, 2], how_sum(5, [2, 3]))
        self.assertEqual(None, how_sum(7, [2, 4]))
        # print(how_sum(5, [2, 3]))

    # def test_02(self):
    #     self.assertEqual(False, how_sum_memo(300, [7, 14]))


if __name__ == '__main__':
    unittest.main()
