import unittest


def count_construct(target, word_bank):

    if target == '':
        return 1

    total = 0

    for x in word_bank:
        if target.find(x) == 0:
            suffix = target[len(x):]
            p = count_construct(suffix, word_bank)
            total += p

    return total


def count_construct_memo(target, word_bank, memo={}):

    if target in memo:
        return memo[target]
    if target == '':
        return 1

    total = 0

    for x in word_bank:
        if target.find(x) == 0:
            suffix = target[len(x):]
            p = count_construct_memo(suffix, word_bank, memo)
            total += p

    memo[target] = total
    return total


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

    ''' This will not work'''
    def test_06(self):
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
