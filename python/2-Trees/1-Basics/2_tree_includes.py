import unittest
from Node import *

"""
    a
   / \
  b   c
 / \   \
d   e   f
"""


def create_tree():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a


def bfs_includes(node, c):

    if node is None:
        return False

    from collections import deque
    queue = deque()

    queue.append(node)

    while len(queue) > 0:

        first_node = queue.popleft()

        if first_node.val == c:
            return True

        if first_node.left:
            queue.append(first_node.left)
        if first_node.right:
            queue.append(first_node.right)

    return False


def dfs_includes(node, c):
    if node is None:
        return False

    if node.val == c:
        return True

    left = dfs_includes(node.left, c)
    right = dfs_includes(node.right, c)

    return left or right

    # return dfs_includes(node.left, c) or dfs_includes(node.right, c)


class MyTestCase(unittest.TestCase):

    def test_bfs_includes_yes(self):
        ans = bfs_includes(create_tree(), 'e')
        self.assertEqual(True, ans)

    def test_bfs_includes_no(self):
        ans = bfs_includes(create_tree(), 'z')
        self.assertEqual(False, ans)

    def test_bfs_includes_no_2(self):
        ans = bfs_includes(None, 'z')
        self.assertEqual(False, ans)

    def test_dfs_includes_yes(self):
        ans = dfs_includes(create_tree(), 'e')
        self.assertEqual(True, ans)

    def test_dfs_includes_no(self):
        ans = dfs_includes(create_tree(), 'z')
        self.assertEqual(False, ans)

    def test_dfs_includes_no_2(self):
        ans = dfs_includes(None, 'z')
        self.assertEqual(False, ans)


if __name__ == '__main__':
    unittest.main()
