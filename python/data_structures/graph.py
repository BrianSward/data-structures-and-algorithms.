class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, value):
        new_node = Vertex(value)
        self.graph_dict[new_node.value] = Vertex(value)
        return new_node

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex.value not in self.graph_dict:
            self.add_vertex(from_vertex)
        if to_vertex.value not in self.graph_dict:
            self.add_vertex(to_vertex)
        self.graph_dict[from_vertex.value].edges[to_vertex.value] = weight
        self.graph_dict[to_vertex.value].edges[from_vertex.value] = weight

    def get_nodes(self):
        return list(self.graph_dict.keys())

    def get_neighbors(self, vertex):
        return self.graph_dict[vertex.value].edges

    def size(self):
        return len(self.graph_dict)


if __name__ == "__main__":
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")

    graph = Graph()

    vertex_a = graph.add_node("A")
    vertex_b = graph.add_node("B")
    # graph.add_node(vertex3)

    graph.add_edge(vertex_a, vertex_b, 5)
    print(graph.get_nodes())
    print(list(graph.get_neighbors(vertex_a).keys()))
    # graph.add_edge(vertex1, vertex4, 9)
    # print(graph.get_neighbors("A"))
    # graph.add_node(Vertex("spam"))
    # print(graph.get_nodes())
    # print(vertex_a.edges)

