import unittest


# Tc = n and SC = n'''
def r1(n):
    if n <= 1:
        return
    r1(n - 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
