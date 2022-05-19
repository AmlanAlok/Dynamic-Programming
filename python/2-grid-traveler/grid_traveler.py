import unittest


'''
Grid Traveler

grid_traveler has TC = 2^(m+n) and SC = m+n

grid_traveler_memo has TC = m*n and SC = m+n
'''


def grid_traveler(m, n):

    if m == 0 or n == 0:
        return 0

    if m == 1 and n == 1:
        return 1

    return grid_traveler(m-1, n) + grid_traveler(m, n-1)



class MyTestCase(unittest.TestCase):

    def test_01(self):

        self.assertEqual(3, grid_traveler(2, 3))
        self.assertEqual(6, grid_traveler(3, 3))




if __name__ == '__main__':
    unittest.main()
