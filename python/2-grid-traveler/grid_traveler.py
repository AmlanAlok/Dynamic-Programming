import unittest


'''
Grid Traveler

grid_traveler has TC = 2^(m+n) and SC = m+n

grid_traveler_memo has TC = m*n and SC = m+n

We are going to have m*n distinct nodes when using memoization
'''


def grid_traveler(m, n):

    if m == 0 or n == 0:
        return 0

    if m == 1 and n == 1:
        return 1

    return grid_traveler(m-1, n) + grid_traveler(m, n-1)


def grid_traveler_memo(m, n, memo={}):

    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0:
        return 0

    if m == 1 and n == 1:
        return 1

    memo[(m, n)] = grid_traveler_memo(m-1, n, memo) + grid_traveler_memo(m, n-1, memo)
    return memo[(m, n)]


class MyTestCase(unittest.TestCase):

    def test_01(self):

        self.assertEqual(3, grid_traveler(2, 3))
        self.assertEqual(6, grid_traveler(3, 3))

    def test_02(self):

        self.assertEqual(3, grid_traveler_memo(2, 3))
        self.assertEqual(6, grid_traveler_memo(3, 3))
        self.assertEqual(35345263800, grid_traveler_memo(20, 20))

    '''
    The classic solution for (20,20) will take a long time to compute
    But the memoized solution will return the answer very quickly 
    '''
    def test_03(self):
        print(grid_traveler_memo(20, 20))
        # print(grid_traveler_memo(2, 2))


if __name__ == '__main__':
    unittest.main()
