class Graph:
    def __init__(self, vertices: list[int], edges: list[tuple[int, int]]) -> None:
        self.vertices = vertices
        self.edges = edges
        self.visited_order = []

    def __iter__(self):
        if not self.visited_order:
            self.dfs()
        return iter(self.visited_order)

    def dfs(self) -> list[int]:
        states = {"w": [v for v in self.vertices], "g": list(), "b": list()}

        def dfs_step(vertex):
            if vertex in states["w"]:
                states["g"].append(vertex)
                states["w"].remove(vertex)
                for edge in self.edges:
                    if edge[0] == vertex:
                        dfs_step(edge[1])
                    if edge[1] == vertex:
                        dfs_step(edge[0])

        for vertex in self.vertices:
            dfs_step(vertex)

        self.visited_order = states["g"]
        return self.visited_order


g = Graph([1, 2, 3], [(1, 3), (2, 3), (2, 1)])

a = g.dfs()
b = list(iter(g))
print(a, b)



