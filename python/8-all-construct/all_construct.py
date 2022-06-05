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

            # if p is not None:
            # f = p[0] + [x]
            for b in p:
                ans.append(b)

    return ans







class MyTestCase(unittest.TestCase):

    def test_something(self):
        # self.assertEqual(True, False)
        print(all_construct('abcdef', ['abc', 'cd', 'def', 'abcd', 'ef', 'd']))


if __name__ == '__main__':
    unittest.main()
