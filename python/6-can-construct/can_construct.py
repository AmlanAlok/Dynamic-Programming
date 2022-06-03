import unittest


def can_construct(target, word_bank):

    if target == '':
        return True

    for x in word_bank:
        if x[0] == target[0]:
            suffix = target[len(x):]

            if can_construct(suffix, word_bank):
                return True

    return False


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(True, can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(False, can_construct("skateboard", ["skat", "te", "bor", "ard"]))
        pass

    def test_03(self):
        self.assertEqual(True, can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
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
