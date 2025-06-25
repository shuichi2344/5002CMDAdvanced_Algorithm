class UDGraph:
    def __init__(self):
        # Initializes an empty graph represented by a dictionary
        # Keys are vertices (e.g., Person objects), and values are sets of adjacent vertices
        self.graph = {}

    def add_vertex(self, vertex):
        # Adds a new vertex to the graph if it's not already present
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def add_edge(self, start, end):
        # Adds a directed edge from 'start' to 'end' if both vertices exist in the graph
        # Used to represent a "follow" relationship (start follows end)
        if start in self.graph and end in self.graph:
            self.graph[start].add(end)

    def remove_edge(self, start, end):
        # Removes a directed edge from 'start' to 'end' if it exists
        # Used when a user unfollows another
        if start in self.graph and end in self.graph[start]:
            self.graph[start].remove(end)

    def list_outgoing_adjacent(self, vertex):
        # Returns a list of all users that the given vertex (user) is following
        return self.graph.get(vertex, [])

    def list_incoming_adjacent(self, vertex):
        # Returns a list of all users who are following the given vertex (user)
        return [v for v, edges in self.graph.items() if vertex in edges]
