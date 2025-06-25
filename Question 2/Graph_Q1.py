class DirectedGraph:
    def __init__(self):
        # Dictionary to hold adjacency list
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Adds a new vertex to the graph if it doesn't already exist.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end):
        """
        Adds a directed edge from 'start' vertex to 'end' vertex.
        """
        if start in self.graph and end in self.graph:
            self.graph[start].append(end)
        else:
            print("One or both vertices not found.")

    def list_outgoing_adjacent_vertex(self, vertex):
        """
        Returns a list of all vertices that the given vertex has outgoing edges to.
        """
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            print(f"Vertex '{vertex}' not found.")
            return []

    def __str__(self):
        """
        Optional: Return a string representation of the graph for debugging.
        """
        return "\n".join(f"{v} -> {self.graph[v]}" for v in self.graph)

if __name__ == "__main__":
    g = DirectedGraph()

    # Add vertices
    for v in ["A", "B", "C", "D"]:
        g.add_vertex(v)

    # Add edges
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")

    # List outgoing edges from vertex A
    print("Outgoing from A:", g.list_outgoing_adjacent_vertex("A"))  # ['B', 'C']

    # Print full graph
    print("\nGraph structure:")
    print(g)
