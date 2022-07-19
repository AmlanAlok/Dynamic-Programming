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


def dfs_min(node):
    if node is None:
        return sys.maxsize
    return min(node.val, min(dfs_min(node.left), dfs_min(node.right)))


def bfs_min(node):
    if node is None:
        return sys.maxsize

    from collections import deque
    q = deque()
    q.append(node)

    m = sys.maxsize

    while len(q) > 0:
        fn = q.popleft()

        m = min(m, fn.val)

        if fn.left:
            q.append(fn.left)
        if fn.right:
            q.append(fn.right)

    return m


class MyTestCase(unittest.TestCase):

    def test_dfs_min(self):
        root = create_num_tree()
        self.assertEqual(1, dfs_min(root))

    def test_bfs_min(self):
        root = create_num_tree()
        self.assertEqual(1, bfs_min(root))


if __name__ == '__main__':
    unittest.main()
