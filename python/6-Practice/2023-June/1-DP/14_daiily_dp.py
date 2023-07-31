import unittest
from copy import deepcopy

fib = [1, 2, 3, 4, 5, 6, 7, 20, 30, 40, 50]
fib_dict = {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    6: 8,
    7: 13,
    8: 21,
    9: 34,
    20: 6765,
    30: 832040,
    40: 102334155,
    50: 12586269025
}


def fib_memo(n, memo=None):
    pass


def grid_traveler_memo(m, n, memo=None):
    pass


def can_sum_memo(t, nums, memo=None):
    pass


def how_sum_memo(t, nums, memo=None):
    pass


def best_sum_memo(t, nums, memo=None):
    pass


def can_construct_memo(t, words, memo=None):
    pass


def count_construct_memo(t, words, memo=None):
    pass


def all_construct_memo(t, words, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == '':
        return [[]]

    ans = []

    for w in words:
        if w == t[:len(w)]:
            new_t = t[len(w):]
            v = deepcopy(all_construct_memo(new_t, words, memo))

            for a in v:
                a.insert(0, w)
            for b in v:
                ans.append(b)

    memo[t] = ans
    return ans


class MyTestCase(unittest.TestCase):

    def test_1(self):
        for i in range(len(fib)):
            n = fib[i]
            self.assertEqual(fib_memo(n), fib_dict[n])

    def test_2(self):
        self.assertEqual(3, grid_traveler_memo(2, 3))
        self.assertEqual(6, grid_traveler_memo(3, 3))
        self.assertEqual(35345263800, grid_traveler_memo(20, 20))

    def test_3(self):
        self.assertEqual(True, can_sum_memo(7, [5, 3, 4, 7]))
        self.assertEqual(True, can_sum_memo(7, [2, 3]))
        self.assertEqual(False, can_sum_memo(7, [2, 4]))
        self.assertEqual(False, can_sum_memo(300, [7, 14]))

    def test_4(self):
        self.assertEqual([4, 3], how_sum_memo(7, [5, 3, 4, 7]))
        self.assertEqual([3, 2, 2], how_sum_memo(7, [2, 3]))
        self.assertEqual([4, 3], how_sum_memo(7, [5, 3, 4, 7]))
        self.assertEqual(None, how_sum_memo(7, [2, 4]))
        self.assertEqual([3, 2], how_sum_memo(5, [2, 3]))
        self.assertEqual(None, how_sum_memo(300, [7, 14]))
        self.assertEqual([100, 100, 100], how_sum_memo(300, [100, 7, 14]))
        self.assertEqual([3, 2, 2], how_sum_memo(7, [2, 3]))

    def test_5(self):
        self.assertEqual([7], best_sum_memo(7, [5, 3, 4, 7]))
        self.assertEqual([5, 3], best_sum_memo(8, [2, 3, 5]))
        self.assertEqual([4, 4], best_sum_memo(8, [1, 4, 5]))
        self.assertEqual([25, 25, 25, 25], best_sum_memo(100, [1, 2, 5, 25]))

    def test_6(self):
        self.assertEqual(True, can_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(False, can_construct_memo("skateboard", ["skat", "te", "bor", "ard"]))
        self.assertEqual(True, can_construct_memo("banana", ["ba", "pa", "ca", "na"]))
        self.assertEqual(True, can_construct_memo('', ["ba", "pa", "ca", "na"]))
        self.assertEqual(False, can_construct_memo("potato", ["pot", "ta", "to"]))
        self.assertEqual(True, can_construct_memo("skateboard", ["skat", "te", "e", "bo", "ard"]))
        self.assertEqual(False, can_construct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
            'e',
            'ee',
            'eee',
            'eeee',
            'eeeee',
            'eeeeee',
            'eeeeeee',
            'eeeeeeee'
        ]))

    def test_7(self):
        self.assertEqual(2, count_construct_memo('abcdef', ['a', 'abc', 'cd', 'def', 'abcd', 'ef']))
        self.assertEqual(1, count_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(3, count_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']))
        self.assertEqual(0, count_construct_memo("skateboard", ["skat", "te", "bor", "ard"]))
        self.assertEqual(0, count_construct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
            'e',
            'ee',
            'eee',
            'eeee',
            'eeeee',
            'eeeeee',
            'eeeeeee',
            'eeeeeeee'
        ]))

    def test_8(self):

        self.assertEqual([
            ['abc', 'def'],
            ['abc', 'd', 'ef'],
            ['abcd', 'ef']
        ],  all_construct_memo('abcdef', ['abc', 'cd', 'def', 'abcd', 'ef', 'd']))

        self.assertEqual([
            ['purp', 'le'],
            ['p', 'ur', 'p', 'le']
        ], all_construct_memo("purple", ['purp', 'p', 'ur', 'le', 'purpl']))

        self.assertEqual([
            ['ab', 'cd', 'ef'],
            ['ab', 'c', 'def'],
            ['abc', 'def'],
            ['abcd', 'ef']
        ], all_construct_memo("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))


if __name__ == '__main__':
    unittest.main()
