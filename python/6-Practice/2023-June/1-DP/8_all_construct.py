import unittest
from copy import deepcopy


def all_construct(t, words):

    if t == '':
        return [[]]

    ans = []

    for w in words:
        p = t[:len(w)]
        if p == w:
            x = t[len(w):]
            v = all_construct(x, words)

            for a in v:
                a.insert(0, w)
            for b in v:
                ans.append(b)
    return ans

'''
If we do not use deepcopy, the ans var returned in the last line of the func 
is referenced as v in the parent function.
So when we manipulate the var v, it changes the memo[t] value which was the ans.
Without deepcopy, ans and v reference the same memory address.
Hence, manipulating one changes the common data.
'''
def all_construct_memo(t, words, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == '':
        return [[]]

    ans = []

    for w in words:
        p = t[:len(w)]
        if p == w:
            x = t[len(w):]
            v = deepcopy(all_construct_memo(x, words, memo))

            for a in v:
                a.insert(0, w)
            for b in v:
                ans.append(b)

    memo[t] = ans
    return ans


class MyTestCase(unittest.TestCase):

    def test_01(self):
        # self.assertEqual(True, False)
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
        # self.assertEqual(True, False)
        # self.assertEqual(True, False)

    # def test_02(self):
    #     print(all_construct("eeeeeeeeeeeeeeef", [
    #         'e',
    #         'ee',
    #         'eee',
    #         'eeee',
    #         'eeeee',
    #         'eeeeee',
    #         'eeeeeee',
    #         'eeeeeeee']))

    def test_03(self):
        # self.assertEqual(True, False)
        self.assertEqual([
            ['abc', 'def'],
            ['abc', 'd', 'ef'],
            ['abcd', 'ef']
        ],  all_construct_memo('abcdef', ['abc', 'cd', 'def', 'abcd', 'ef', 'd']))

    def test_04(self):
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
