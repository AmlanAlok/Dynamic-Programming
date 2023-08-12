import unittest
from copy import deepcopy


def all_construct(target, word_bank):

    if target == '':
        return [[]]

    ans = []

    for x in word_bank:

        if target.find(x) == 0:
            suffix = target[len(x):]
            p = all_construct(suffix, word_bank)

            for a in p:
                a.insert(0, x)

            for b in p:
                ans.append(b)

    return ans


# def all_construct_memo(target, word_bank, memo=None):
#
#     if memo is None:
#         memo = {}
#     if target in memo:
#         return memo[target]
#     if target == '':
#         return [[]]
#
#     ans = []
#
#     for x in word_bank:
#
#         if target.find(x) == 0:
#             suffix = target[len(x):]
#             p = deepcopy(all_construct_memo(suffix, word_bank, memo))
#
#             for a in p:
#                 a.insert(0, x)
#
#             for b in p:
#                 ans.append(b)
#
#     memo[target] = ans
#     return ans

def all_construct_memo(target, word_bank, memo={}):

    if target in memo:
        return memo[target]
    if target == '':
        return [[]]

    ans = []

    for x in word_bank:

        if target.find(x) == 0:
            suffix = target[len(x):]
            p = deepcopy(all_construct_memo(suffix, word_bank, memo))

            for a in p:
                a.insert(0, x)

            for b in p:
                ans.append(b)

    memo[target] = ans
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
        """
        If you run both the assert statements in a single execution with memo={}, it will fail.
        Bcuz the memo will be initialized once when func is initiated and then the same memo will be
        used in the 2nd assert statement.

        This is from the PyCharm warning that default argument is mutable.


        :return:
        """
        # self.assertEqual(True, False)
        self.assertEqual([
            ['abc', 'def'],
            ['abc', 'd', 'ef'],
            ['abcd', 'ef']
        ],  all_construct_memo('abcdef', ['abc', 'cd', 'def', 'abcd', 'ef', 'd']))

        self.assertEqual([
            ['ab', 'cd', 'ef'],
            ['ab', 'c', 'def'],
            ['abc', 'def'],
            ['abcd', 'ef']
        ], all_construct_memo("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))

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
