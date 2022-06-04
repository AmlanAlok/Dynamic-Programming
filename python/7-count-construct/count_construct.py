import unittest


def count_construct(target, word_bank):


class MyTestCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(True, True)
        self.assertEqual(1, count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
        self.assertEqual(1, count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']))


if __name__ == '__main__':
    unittest.main()
