import unittest
"""
a -> c
|    |
b    e   
|
d -> f
"""


def get_graph():

    return {
        'a': ['c', 'b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }


def dfs_stack(graph, src):

    from collections import deque
    stack = deque()

    stack.append(src)
    ans = []

    while len(stack) > 0:
        last = stack.pop()
        ans.append(last)

        for c in graph[last]:
            stack.append(c)

    return ans


def dfs_recur(g, src):

    p = [src]

    for n in g[src]:
        x = dfs_recur(g, n)
        p = p + x

    return p


class MyTestCase(unittest.TestCase):

    def test_dfs_stack(self):
        self.assertEqual(['a', 'b', 'd', 'f', 'c', 'e'], dfs_stack(get_graph(), 'a'))

    def test_dfs_recur(self):
        self.assertEqual(['a', 'c', 'e', 'b', 'd', 'f'], dfs_recur(get_graph(), 'a'))


if __name__ == '__main__':
    unittest.main()
