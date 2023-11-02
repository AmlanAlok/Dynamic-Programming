import unittest
from copy import deepcopy

fib_n = [1, 2, 3, 4, 5, 6, 7, 20, 30, 40, 50]
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


def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    v = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = v
    return v


def grid_traveler(m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    v = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    memo[(m, n)] = v
    return v


def can_sum(t, nums, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == 0:
        return True
    if t < 0:
        return False

    for n in nums:
        new_t = t-n

        v = can_sum(new_t, nums, memo)
        memo[new_t] = v
        if v:
            return True
    return False


def how_sum(t, nums, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == 0:
        return []
    if t < 0:
        return None

    for n in nums:
        new_t = t-n

        v = how_sum(new_t, nums, memo)
        memo[new_t] = v
        if v is not None:
            v = v + [n]
            return v
    return None


def best_sum(t, nums, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == 0:
        return []
    if t < 0:
        return None

    ans = None

    for n in nums:
        new_t = t-n

        v = best_sum(new_t, nums, memo)

        if v is not None:
            v = v + [n]
            # v.append(n)   # using this will fail the code as
            # print(v)
            # new_v = deepcopy(v)
            if ans is None or len(v) < len(ans):
                ans = v
    memo[t] = ans
    return ans


def can_construct(t, words, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == '':
        return True

    for w in words:
        if w == t[:len(w)]:
            new_t = t[len(w):]

            v = can_construct(new_t, words, memo)
            memo[new_t] = v

            if v:
                return True
    return False


def count_construct(t, words, memo=None):
    pass


def all_construct(t, words, memo=None):
    pass



class MyTestCase(unittest.TestCase):

    def test_1(self):
        for i in range(len(fib_n)):
            n = fib_n[i]
            self.assertEqual(fib(n), fib_dict[n])

    def test_2(self):
        self.assertEqual(3, grid_traveler(2, 3))
        self.assertEqual(6, grid_traveler(3, 3))
        self.assertEqual(35345263800, grid_traveler(20, 20))

    def test_3(self):
        self.assertEqual(True, can_sum(7, [5, 3, 4, 7]))
        self.assertEqual(True, can_sum(7, [2, 3]))
        self.assertEqual(False, can_sum(7, [2, 4]))
        self.assertEqual(False, can_sum(300, [7, 14]))

    def test_4(self):
        self.assertEqual([4, 3], how_sum(7, [5, 3, 4, 7]))
        self.assertEqual([3, 2, 2], how_sum(7, [2, 3]))
        self.assertEqual([4, 3], how_sum(7, [5, 3, 4, 7]))
        self.assertEqual(None, how_sum(7, [2, 4]))
        self.assertEqual([3, 2], how_sum(5, [2, 3]))
        self.assertEqual(None, how_sum(300, [7, 14]))
        self.assertEqual([100, 100, 100], how_sum(300, [100, 7, 14]))
        self.assertEqual([3, 2, 2], how_sum(7, [2, 3]))

    def test_5(self):
        self.assertEqual([7], best_sum(7, [5, 3, 4, 7]))
        self.assertEqual([5, 3], best_sum(8, [2, 3, 5]))
        self.assertEqual([4, 4], best_sum(8, [1, 4, 5]))
        self.assertEqual([25, 25, 25, 25], best_sum(100, [1, 2, 5, 25]))

    def test_6(self):
        self.assertEqual(True, can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(False, can_construct("skateboard", ["skat", "te", "bor", "ard"]))
        self.assertEqual(True, can_construct("banana", ["ba", "pa", "ca", "na"]))
        self.assertEqual(True, can_construct('', ["ba", "pa", "ca", "na"]))
        self.assertEqual(False, can_construct("potato", ["pot", "ta", "to"]))
        self.assertEqual(True, can_construct("skateboard", ["skat", "te", "e", "bo", "ard"]))
        self.assertEqual(False, can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
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
        self.assertEqual(2, count_construct('abcdef', ['a', 'abc', 'cd', 'def', 'abcd', 'ef']))
        self.assertEqual(1, count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(3, count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']))
        self.assertEqual(0, count_construct("skateboard", ["skat", "te", "bor", "ard"]))
        self.assertEqual(0, count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
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
        ],  all_construct('abcdef', ['abc', 'cd', 'def', 'abcd', 'ef', 'd']))

        self.assertEqual([
            ['purp', 'le'],
            ['p', 'ur', 'p', 'le']
        ], all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))

        self.assertEqual([
            ['ab', 'cd', 'ef'],
            ['ab', 'c', 'def'],
            ['abc', 'def'],
            ['abcd', 'ef']
        ], all_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))


if __name__ == '__main__':
    unittest.main()
