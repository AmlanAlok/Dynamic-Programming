import unittest
from Node import *


def insert(root, val):

    if root is None:
        return Node(val)
    elif val == root.val:
        print('Already exists')
    elif val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)

    return root


def inorder(root):

    # p = []
    #
    # if root.left:
    #     p += inorder(root.left)
    # if root:
    #     p += [root.val]
    # if root.right:
    #     p += inorder(root.right)
    #
    # return p

    if root is None:
        return []

    return inorder(root.left) + [root.val] + inorder(root.right)


def inorder_2(root):

    p = []

    if root.left:
        p += inorder(root.left)
    if root:
        p += [root.val]
    if root.right:
        p += inorder(root.right)

    return p


class MyTestCase(unittest.TestCase):

    def test_something(self):
        root = None
        root = insert(root, 8)
        root = insert(root, 3)
        root = insert(root, 1)
        root = insert(root, 6)
        root = insert(root, 7)
        root = insert(root, 10)
        root = insert(root, 14)
        root = insert(root, 4)

        print(inorder(root))

        self.assertEqual([1, 3, 4, 6, 7, 8, 10, 14], inorder(root))
        self.assertEqual([1, 3, 4, 6, 7, 8, 10, 14], inorder_2(root))


if __name__ == '__main__':
    unittest.main()
