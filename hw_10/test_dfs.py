from dfs import Graph

graph = Graph([1, 2, 3], [(1, 3), (2, 3), (2, 1)])

def test_1():
    g = graph.dfs()
    assert g == [1, 3, 2]

def test_2():
    g = list(iter(graph))
    assert g == [1, 3, 2]