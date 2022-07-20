import unittest
from Node import *
import sys
"""
    a
   / \
  b   c
 / \   \
d   e   f
"""


def create_num_tree():
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a


def max_sum_path(node, s):
    if node is None:
        return s

    s += node.val
    left = max_sum_path(node.left, s)
    right = max_sum_path(node.right, s)

    return max(left, right)


'''Better Code'''


def max_path(node):
    if node is None:
        return -sys.maxsize

    left = max_path(node.left)
    right = max_path(node.right)

    if max(left, right) == -sys.maxsize:
        return node.val
    return node.val + max(left, right)


def alvin_max_path(node):
    if node is None:
        return -sys.maxsize
    if node.left is None and node.right is None:
        return node.val

    max_child = max(alvin_max_path(node.left), alvin_max_path(node.right))
    return node.val + max_child


class MyTestCase(unittest.TestCase):

    def test_max_sum_path(self):
        root = create_num_tree()
        self.assertEqual(20, max_sum_path(root, 0))

    def test_max_sum_path_bottom_up(self):
        root = create_num_tree()
        self.assertEqual(20, max_path(root))

    def test_max_sum_path_bottom_up_none(self):
        self.assertEqual(-sys.maxsize, max_path(None))

    def test_max_sum_path_bottom_up_alvin(self):
        root = create_num_tree()
        self.assertEqual(20, alvin_max_path(root))

    def test_max_sum_path_none(self):
        self.assertEqual(0, max_sum_path(None, 0))


if __name__ == '__main__':
    unittest.main()
