"""
    a
   / \
  b   c
 / \   \
d   e   f
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    ''' Recursive DFS'''
    def dfs_rec(self, node):

        if node is None:
            return

        print(node.val)

        if node.left:
            self.dfs_rec(node.left)
        if node.right:
            self.dfs_rec(node.right)

    ''' Stack DFS '''
    def dfs_stack(self, node):
        from collections import deque
        stack = deque()

        stack.append(node)

        while len(stack) != 0:

            last_node = stack.pop()
            print(last_node.val)

            if last_node.right:
                stack.append(last_node.right)
            if last_node.left:
                stack.append(last_node.left)

        return


def run():
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

    # a.dfs_rec(a)
    a.dfs_stack(a)
    pass


if __name__ == '__main__':
    run()
