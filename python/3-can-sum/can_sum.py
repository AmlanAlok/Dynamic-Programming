import unittest


def can_sum(target_sum, numbers):

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for n in numbers:
        remainder = target_sum - n

        if can_sum(remainder, numbers):
            return True

    return False


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(True, can_sum(7, [5, 3, 4, 7]))
        self.assertEqual(True, can_sum(7, [2, 3]))
        self.assertEqual(False, can_sum(7, [2, 4]))



if __name__ == '__main__':
    unittest.main()
