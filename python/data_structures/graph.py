class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_node(self, value):
        new_node = Vertex(value)
        self.graph_dict[new_node] = []
        return new_node

    def add_edge(self, start, end, weight=0):
        if end not in self.graph_dict:
            raise KeyError("End vertex is not in the graph")
        self.graph_dict[start].append(Edge(end, weight))

    def get_nodes(self):
        return list(self.graph_dict.keys())

    def get_neighbors(self, vertex):
        return self.graph_dict[vertex]

    def size(self):
        return len(self.graph_dict)

    def depth_first_search(self, vertex):
        visited = []
        self.depth_first_helper(vertex, visited)
        return visited

    def depth_first_helper(self, vertex, visited):
        if vertex not in self.graph_dict:
            return
        visited.append(vertex.value)
        for edge in self.graph_dict[vertex]:
            if edge.vertex.value not in visited:
                self.depth_first_helper(edge.vertex, visited)

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


