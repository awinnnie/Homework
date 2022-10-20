class Graph():
    def __init__(self, g_dict = None):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict
    def get_vertex(self):
        return list(self.g_dict.keys())
    def get_edges(self):
        edg = []
        for i in list(self.g_dict.items()):
            for j in i[1]:
                if tuple(reversed((i[0], j))) not in edg:
                    edg.append((i[0], j))
        return edg
    def add_vertex(self,vertex):
        self.g_dict[vertex] = []
    def add_edge(self, new_edge):
        if new_edge[0] in self.g_dict:
            if new_edge[1] not in self.g_dict[new_edge[0]]:
                self.g_dict[new_edge[0]].extend(new_edge[1])
        else:
            self.g_dict[new_edge[0]] = new_edge[1]
        
graph1 = Graph({"a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["b", "c", "e"],
    "e": ["d"]
})

graph1.add_vertex("f")
graph1.add_edge(("o", "a"))
print(graph1.get_vertex())
print(graph1.get_edges())