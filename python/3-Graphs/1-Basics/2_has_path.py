import unittest
'''
n = # nodes
e = # edges
TC = O(e) bcuz you will have to travel through every single edge of our graph
SC = O(n) bcuz you will have to have every single node on the stack
'''

# adjacency lust
def get_graph():

    return {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }


def dfs_has_path(g, src, dst):

    if src == dst:
        return True

    p = []

    for n in g[src]:
        p.append(dfs_has_path(g, n, dst))

    return True in p


def bfs_has_path(g, src, dst):

    from collections import deque
    q = deque()
    q.append(src)

    while len(q) > 0:
        fn = q.popleft()

        if fn == dst:
            return True

        for n in g[fn]:
            q.append(n)

    return False


class MyTestCase(unittest.TestCase):

    def test_dfs_has_path_true(self):
        self.assertEqual(True, dfs_has_path(get_graph(), 'f', 'k'))

    def test_dfs_has_path_false(self):
        self.assertEqual(False, dfs_has_path(get_graph(), 'j', 'f'))

    def test_bfs_has_path_true(self):
        self.assertEqual(True, bfs_has_path(get_graph(), 'f', 'k'))

    def test_bfs_has_path_false(self):
        self.assertEqual(False, bfs_has_path(get_graph(), 'j', 'f'))


if __name__ == '__main__':
    unittest.main()
