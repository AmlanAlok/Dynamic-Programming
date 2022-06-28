import unittest

'''
TC = n^m + m
SC = m * m = m^2
'''


def best_sum(target_sum, numbers):

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_ans = None

    for n in numbers:
        remainder = target_sum - n
        # ans.append(n)

        ans = best_sum(remainder, numbers)
        if ans is not None:
            # in the worst case this operation will take m steps
            new_ans = ans + [n]         # ans.append(n) returns None
            if shortest_ans is None or len(new_ans) < len(shortest_ans):
                shortest_ans = new_ans

    return shortest_ans


def best_sum_memo(target_sum, numbers, memo={}):

    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_ans = None

    for n in numbers:
        remainder = target_sum - n

        ans = best_sum_memo(remainder, numbers, memo)
        if ans is not None:
            # in the worst case this operation will take m steps
            new_ans = ans + [n]         # ans.append(n) returns None
            if shortest_ans is None or len(new_ans) < len(shortest_ans):
                shortest_ans = new_ans

    memo[target_sum] = shortest_ans
    return shortest_ans


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual([7], best_sum(7, [5, 3, 4, 7]))
        self.assertEqual([5, 3], best_sum(8, [2, 3, 5]))
        self.assertEqual([4, 4], best_sum(8, [1, 4, 5]))

    ''' This will take a very long time '''
    def test_03(self):
        self.assertEqual([25, 25, 25, 25], best_sum(100, [1, 2, 5, 25]))

    def test_04(self):
        self.assertEqual([25, 25, 25, 25], best_sum_memo(100, [1, 2, 5, 25]))


if __name__ == '__main__':
    unittest.main()
