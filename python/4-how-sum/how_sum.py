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


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual([4, 3], how_sum(7, [5, 3, 4, 7]))
        self.assertEqual([3, 2, 2], how_sum(7, [2, 3]))
        self.assertEqual([3, 2], how_sum(5, [2, 3]))
        self.assertEqual(None, how_sum(7, [2, 4]))
        # print(how_sum(5, [2, 3]))


if __name__ == '__main__':
    unittest.main()
