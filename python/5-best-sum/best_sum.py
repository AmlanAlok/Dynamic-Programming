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

    def test_something(self):
        self.assertEqual([7], best_sum(7, [5, 3, 4, 7]))
        # print(best_sum(7, [5, 3, 4, 7]))


if __name__ == '__main__':
    unittest.main()
