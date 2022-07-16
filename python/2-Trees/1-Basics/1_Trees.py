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


def bfs_queue(node):
    if node is None:
        return []

    from collections import deque
    queue = deque()
    result = []

    queue.append(node)

    while len(queue) > 0:

        first_node = queue.popleft()
        result.append(first_node.val)

        if first_node.left:
            queue.append(first_node.left)
        if first_node.right:
            queue.append(first_node.right)

    return result


def bfs_includes(node, c):

    if node is None:
        return []

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


class MyTestCase(unittest.TestCase):

    def test_dfs_rec(self):
        ans = dfs_rec(create_tree())
        # print(ans)
        self.assertEqual(['a', 'b', 'd', 'e', 'c', 'f'], ans)

    def test_dfs_stack(self):
        ans = dfs_stack(create_tree())
        # print(ans)
        self.assertEqual(['a', 'b', 'd', 'e', 'c', 'f'], ans)

    def test_bfs_queue(self):
        ans = bfs_queue(create_tree())
        # print(ans)
        self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f'], ans)

    def test_bfs_includes_yes(self):
        ans = bfs_includes(create_tree(), 'e')
        # print(ans)
        self.assertEqual(True, ans)

    def test_bfs_includes_no(self):
        ans = bfs_includes(create_tree(), 'z')
        # print(ans)
        self.assertEqual(False, ans)


if __name__ == '__main__':
    unittest.main()
