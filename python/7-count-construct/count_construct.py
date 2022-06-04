import unittest


def count_construct(target, word_bank):

    if target == '':
        return 1

    total = 0

    for x in word_bank:
        if target.find(x) == 0:
            suffix = target[len(x):]
            p = count_construct(suffix, word_bank)

            if p is not None:
                total += p

    return total


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(True, True)
        self.assertEqual(1, count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(2, count_construct('abcdef', ['a', 'abc', 'cd', 'def', 'abcd', 'ef']))
        self.assertEqual(3, count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']))


if __name__ == '__main__':
    unittest.main()
