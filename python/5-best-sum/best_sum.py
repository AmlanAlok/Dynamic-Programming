import unittest


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


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual([7], best_sum(7, [5, 3, 4, 7]))
        self.assertEqual([5, 3], best_sum(8, [2, 3, 5]))
        self.assertEqual([4, 4], best_sum(8, [1, 4, 5]))
        # print(best_sum(7, [5, 3, 4, 7]))


if __name__ == '__main__':
    unittest.main()
