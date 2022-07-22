import unittest


def get_edges():
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]

    return edges


def make_adjacency_list(edges):

    d = {}

    for [x, y] in edges:
        d = add_edges(x, y, d)
        d = add_edges(y, x, d)

    return d


def add_edges(x, y, d):

    if x in d:
        d[x].append(y)
    else:
        d[x] = [y]

    return d



def dfs_undirected_graph(edges, src, dst):
    pass


class MyTestCase(unittest.TestCase):

    def test_something(self):
        adj_list = make_adjacency_list(edges=get_edges())
        self.assertEqual({
            'i': ['j', 'k'],
            'j': ['i'],
            'k': ['i', 'm', 'l'],
            'm': ['k'],
            'l': ['k'],
            'o': ['n'],
            'n': ['o']
        }, adj_list)


if __name__ == '__main__':
    unittest.main()
