import unittest


def can_construct(t, words):
    if t == '':
        return True

    for w in words:
        p = t[:len(w)]
        if p == w:
            x = t[len(w):]
            if can_construct(x, words):
                return True
    return False


# https://stackoverflow.com/questions/41686829/why-does-pycharm-warn-about-mutable-default-arguments-how-can-i-work-around-the#:~:text=Default%20arguments%20value%20is%20mutable&text=Default%20argument%20values%20are%20evaluated,subsequent%20calls%20of%20the%20function
"""
If you want to change immutable objects another object is created - but if you change 
mutable objects the object remains the same but it's contents are changed.

The tricky part is that class variables and default arguments are created when the function 
is loaded (and only once), that means that any changes to a "mutable default argument" 
or "mutable class variable" are permanent
"""


def can_construct_memo(t, words, memo=None):
    if memo is None:
        memo = {}
    if t in memo:
        return memo[t]
    if t == '':
        return True

    for w in words:
        p = t[:len(w)]
        if p == w:
            x = t[len(w):]
            memo[x] = can_construct_memo(x, words, memo)
            if memo[x]:
                return True
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

    def test_04(self):
        print(can_construct_memo("skateboard", ["skat", "te", "e", "bo", "ard"]))
        self.assertEqual(True, can_construct_memo("skateboard", ["skat", "te", "e", "bo", "ard"]))

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
