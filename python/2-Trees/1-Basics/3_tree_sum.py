import unittest
from Node import *

"""
    a
   / \
  b   c
 / \   \
d   e   f
"""


def create_num_tree():
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a


def dfs_tree_sum(node):
    return recur(node, 0)


def recur(node, s):
    if node is None:
        return s

    left_sum = recur(node.left, s + node.val)
    right = recur(node.right, left_sum)

    return right


def bfs_tree_sum(node):
    if node is None:
        return 0

    from collections import deque
    q = deque()
    s = 0

    q.append(node)

    while len(q) > 0:
        fn = q.popleft()
        s += fn.val

        if fn.left:
            q.append(fn.left)
        if fn.right:
            q.append(fn.right)

    return s


class MyTestCase(unittest.TestCase):

    def test_dfs_tree_sum(self):
        ans = dfs_tree_sum(create_num_tree())
        self.assertEqual(25, ans)

    def test_dfs_tree_sum_none(self):
        ans = dfs_tree_sum(None)
        self.assertEqual(0, ans)

    def test_bfs_tree_sum(self):
        ans = bfs_tree_sum(create_num_tree())
        self.assertEqual(25, ans)

    def test_bfs_tree_sum_none(self):
        ans = bfs_tree_sum(None)
        self.assertEqual(0, ans)


if __name__ == '__main__':
    unittest.main()
