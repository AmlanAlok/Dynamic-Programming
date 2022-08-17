import unittest
from Node import *


def search(root, val):

    if root is None:
        return False
    elif val == root.val:
        return True
    elif val < root.val:
        return search(root.left, val)
    elif val > root.val:
        return search(root.right, val)


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


def deletion(root, val):

    if root is None:
        return root
    elif val == root.val:
        if root.left is None and root.right is None:
            root = None
        elif root.left is not None:
            root.val = root.left.val
            root.left = None
        elif root.right is not None:
            root.val = root.right.val
            root.right = None
        elif root.left is not None and root.right is not None:
            print('two child scenario')
    elif val < root.val:
        root.left = deletion(root.left, val)
    elif val > root.val:
        root.right = deletion(root.right, val)

    return root


def inorder(root):

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


def pre_order(root):

    if root is None:
        return []

    return [root.val] + pre_order(root.left) + pre_order(root.right)


def post_order(root):

    if root is None:
        return []

    return post_order(root.left) + post_order(root.right) + [root.val]


class MyTestCase(unittest.TestCase):

    """
           8
         /   \
        3     10
       / \      \
      1   6      14
         / \
        4   7
    """
    def setUp(self) -> None:
        self.root = None
        self.root = insert(self.root, 8)
        self.root = insert(self.root, 3)
        self.root = insert(self.root, 1)
        self.root = insert(self.root, 6)
        self.root = insert(self.root, 7)
        self.root = insert(self.root, 10)
        self.root = insert(self.root, 14)
        self.root = insert(self.root, 4)

    def tearDown(self) -> None:
        del self.root
    
    def test_traversals(self):
        self.assertEqual([1, 3, 4, 6, 7, 8, 10, 14], inorder(self.root))
        self.assertEqual([1, 3, 4, 6, 7, 8, 10, 14], inorder_2(self.root))
        self.assertEqual([8, 3, 1, 6, 4, 7, 10, 14], pre_order(self.root))
        self.assertEqual([1, 4, 7, 6, 3, 14, 10, 8], post_order(self.root))

    def test_search(self):
        root = None
        root = insert(root, 8)
        root = insert(root, 3)
        root = insert(root, 1)
        root = insert(root, 6)
        root = insert(root, 7)
        root = insert(root, 10)
        root = insert(root, 14)
        root = insert(root, 4)

        inorder_nums = [1, 3, 4, 6, 7, 8, 10, 14]
        for i in inorder_nums:
            self.assertEqual(True, search(root, i))

        not_in_nums = [2, 5, 9, 11, 12, 13, 15]
        for i in not_in_nums:
            self.assertEqual(False, search(root, i))

    def test_deletion(self):
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

        # x = deletion(root, 10)
        self.assertEqual([1, 3, 4, 6, 7, 8, 10, 14], inorder(root))
        self.assertEqual([1, 3, 4, 6, 7, 8, 14], inorder(deletion(root, 10)))
        self.assertEqual([1, 3, 6, 7, 8, 14], inorder(deletion(root, 4)))

        # print(inorder(x))




if __name__ == '__main__':
    unittest.main()
