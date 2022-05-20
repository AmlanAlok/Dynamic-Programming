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

        pass



if __name__ == '__main__':
    unittest.main()
