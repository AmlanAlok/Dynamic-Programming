import unittest


'''
Problem 1: Fibonacci Sequence

Fib has TC = 2^n and SC = n

Fib_memo has TC = n and SC = n
'''


def fib(n):

    if n <= 2:
        return 1

    return fib(n-1) + fib(n-2)


def fib_memo(n, memo = {}):

    if n in memo:
        return memo[n]

    if n<=2:
        return 1

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

    return memo[n]


def fib_table(n):

    nums = [0] * (n+1)
    nums[1] = 1

    for i in range(2, len(nums)):
        nums[i] = nums[i-1] + nums[i-2]

    return nums[n]


class MyTestCase(unittest.TestCase):

    def test_something(self):

        self.assertEqual(8, fib(6))
        self.assertEqual(13, fib(7))

    ''' This fib(50) will take a long time with classic recursion method'''
    def test_02(self):
        print('hello')
        # print(fib(50))
        # self.assertEqual(8, fib(6))

    ''' This test uses the fib_memo logic and it is very fast'''
    def test_03(self):
        self.assertEqual(8, fib_memo(6))
        self.assertEqual(13, fib_memo(7))
        self.assertEqual(12586269025, fib_memo(50))
        # print(fib_memo(50))

    def test_table_01(self):
        self.assertEqual(8, fib_table(6))
        self.assertEqual(13, fib_table(7))
        self.assertEqual(12586269025, fib_table(50))


if __name__ == '__main__':
    unittest.main()
