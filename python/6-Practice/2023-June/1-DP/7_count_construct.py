import unittest


def count_construct(t, words):

    if t == '':
        return 1

    count = 0

    for w in words:
        p = t[:len(w)]

        if p == w:
            x = t[len(w):]
            count += count_construct(x, words)

    return count


def count_construct_memo(t, words, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == '':
        return 1

    count = 0

    for w in words:
        p = t[:len(w)]

        if p == w:
            x = t[len(w):]
            count += count_construct_memo(x, words, memo)

    memo[t] = count
    return count


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(True, True)
        self.assertEqual(1, count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(2, count_construct('abcdef', ['a', 'abc', 'cd', 'def', 'abcd', 'ef']))
        self.assertEqual(3, count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']))
        self.assertEqual(0, count_construct("skateboard", ["skat", "te", "bor", "ard"]))

    def test_02(self):
        # self.assertEqual(True, True)
        # self.assertEqual(1, count_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(2, count_construct_memo('abcdef', ['a', 'abc', 'cd', 'def', 'abcd', 'ef']))

    def test_03(self):
        self.assertEqual(1, count_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        print(count_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))

    def test_04(self):
        self.assertEqual(3, count_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']))

    def test_05(self):
        self.assertEqual(0, count_construct_memo("skateboard", ["skat", "te", "bor", "ard"]))

        # print(count_construct_memo('abcdef', ['a', 'abc', 'cd', 'def', 'abcd', 'ef']))

    # ''' This will not work'''
    # def test_06(self):
    #     self.assertEqual(0, count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    #         'e',
    #         'ee',
    #         'eee',
    #         'eeee',
    #         'eeeee',
    #         'eeeeee',
    #         'eeeeeee',
    #         'eeeeeeee'
    #     ]))

    ''' This uses memoization and hence will work '''
    def test_07(self):
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


if __name__ == '__main__':
    unittest.main()
