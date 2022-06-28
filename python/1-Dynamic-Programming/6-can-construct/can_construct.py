import unittest


def can_construct(target, word_bank):

    if target == '':
        return True

    for x in word_bank:
        if target.find(x) == 0:
            suffix = target[len(x):]

            if can_construct(suffix, word_bank):
                return True

    return False


def can_construct_memo(target, word_bank, memo={}):

    if target in memo:
        return memo[target]
    if target == '':
        return True

    for x in word_bank:
        if target.find(x) == 0:
            suffix = target[len(x):]

            memo[target] = can_construct_memo(suffix, word_bank, memo)
            if memo[target]:
                return True

    memo[target] = False
    return False


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(True, can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(False, can_construct("skateboard", ["skat", "te", "bor", "ard"]))
        # self.assertEqual(False,)
        self.assertEqual(True, can_construct("banana", ["ba", "pa", "ca", "na"]))
        self.assertEqual(True, can_construct("", ["ba", "pa", "ca", "na"]))
        self.assertEqual(False, can_construct("potato", ["pot", "ta", "to"]))
        self.assertEqual(True, can_construct("skateboard", ["skat", "te", 'e', "bo", "ard"]))

    def test_02(self):
        self.assertEqual(True, can_construct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(False, can_construct_memo("skateboard", ["skat", "te", "bor", "ard"]))
        self.assertEqual(True, can_construct_memo("banana", ["ba", "pa", "ca", "na"]))
        self.assertEqual(True, can_construct_memo('', ["ba", "pa", "ca", "na"]))
        self.assertEqual(False, can_construct_memo("potato", ["pot", "ta", "to"]))

    # def test_04(self):
    #     print(can_construct_memo("skateboard", ["skat", "te", "e", "bo", "ard"]))
    #     self.assertEqual(True, can_construct_memo("skateboard", ["skat", "te", "e", "bo", "ard"]))

    def test_03(self):
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


if __name__ == '__main__':
    unittest.main()
