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


''' Recursive DFS'''


def dfs_rec(node):
    if node is None:
        return []

    # print(node.val)

    # if node.left:
    left_val = dfs_rec(node.left)
    # if node.right:
    right_val = dfs_rec(node.right)

    return [node.val] + left_val + right_val  # right way
    # return [node.val] + [left_val] + [right_val]    # Incorrect way


'''
Stack DFS
TC = n
SC = n
'''


def dfs_stack(node):
    if node is None:
        return []

    from collections import deque
    stack = deque()
    result = []

    stack.append(node)

    while len(stack) > 0:

        last_node = stack.pop()
        result.append(last_node.val)
        # print(last_node.val)

        if last_node.right:
            stack.append(last_node.right)
        if last_node.left:
            stack.append(last_node.left)

    return result


'''
Stack BFS
TC = n 
SC = n
'''


def bfs_stack(node):
    if node is None:
        return []

    from collections import deque
    stack = deque()
    result = []

    stack.append(node)

    while len(stack) > 0:

        last_node = stack.popleft()
        result.append(last_node.val)

        if last_node.left:
            stack.append(last_node.left)
        if last_node.right:
            stack.append(last_node.right)

    return result


class MyTestCase(unittest.TestCase):

    def test_dfs_rec(self):
        ans = dfs_rec(create_tree())
        # print(ans)
        self.assertEqual(['a', 'b', 'd', 'e', 'c', 'f'], ans)

    def test_dfs_stack(self):
        ans = dfs_stack(create_tree())
        # print(ans)
        self.assertEqual(['a', 'b', 'd', 'e', 'c', 'f'], ans)

    def test_bfs_stack(self):
        ans = bfs_stack(create_tree())
        # print(ans)
        self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f'], ans)


if __name__ == '__main__':
    unittest.main()
