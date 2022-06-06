import unittest


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

    def test_02(self):
        print(all_construct("eeeeeeeeeeeeeeef", [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee',
    'eeeeeee',
    'eeeeeeee']))


if __name__ == '__main__':
    unittest.main()
