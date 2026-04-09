
class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = {}  # Initialize an empty dictionary to store the adjacency list
        self.weights = {}
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []  # Add a new vertex with an empty list of edges

    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 in self.graph and vertex2 in self.graph: # Check that vertices are present
            # store vertex and weight as a tuple
            self.graph[vertex1].append(vertex2)
            if self.weighted:
                self.weights[(vertex1, vertex2)] = weight
            if not self.directed: # In the case of an undirected graph, append in both directions
                self.graph[vertex2].append(vertex1)
                if self.weighted:
                    self.weights[(vertex2, vertex1)] = weight
        else:
            print("One or both vertices not found in graph.")

    # CHALLENGE
    # Write functions to remove vertices and edges from the graph!
    def remove_vertex(self, vertex):
        if vertex in self.graph: # If vertex is present
            # Remove associated edges
            edges_to_remove = [] # We dont want to delete while iterating over a collection, this is bad practice
            for k in self.graph: # for every vertex in the graph
                for v in self.graph[k]: # for every neighbor vertex in the edge list 
                    if v == vertex:
                        edges_to_remove.append((k,v))
            
            for e in edges_to_remove:
                self.remove_edge(e[0], e[1])

            # remove vertex
            del self.graph[vertex]
        else:
            print("vertex not present in graph.")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph and vertex2 in self.graph[vertex1]: # vertices and edge must exist
            self.graph[vertex1].remove(vertex2)
            if not self.directed:
                self.graph[vertex2].remove(vertex1) # If not directed, remove both!
        else:
            print("edge not present in graph.")

    # print graph representation
    # This requires the vertices to be representable as strings
    def print_graph(self):
        for vertex in self.graph: 
            if len(self.graph[vertex]) == 0: # If there are no neighbors of this vertex, just print the vertex itself
                print(vertex)
            else: # if there are neighbors
                if self.directed:
                        print(f"{vertex} --> {' '.join([neighbor if not self.weighted else neighbor + str(self.weights[(vertex, neighbor)]) for neighbor in self.graph[vertex]])}")
                else:
                    print(f"{vertex} --- {' '.join([neighbor if not self.weighted else neighbor + str(self.weights[(vertex, neighbor)]) for neighbor in self.graph[vertex]])}")

    # Breadth First Search algorithm
    def bfs(self, start_vertex):
        visited = {start_vertex}
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0) # FIFO behavior
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print()
        return visited
        
    # Depth First Search algorithm
    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            vertex = stack.pop() # LIFO behavior
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
        print()
        return visited


    def cycle_dfs(self, current_vertex, visited: set, parent_vertex):
        visited.add(current_vertex)

        for neighbor in self.graph[current_vertex]:
            if neighbor not in visited:
                if self.cycle_dfs(neighbor, visited, current_vertex):
                    return True
            elif parent_vertex != neighbor:
                return True

        return False

    def has_undirected_cycle(self):
        visited = set()

        for vertex in self.graph:
            if vertex not in visited:
                if self.cycle_dfs(vertex, visited, None):
                    return True

        return False
    
    def directed_cycle_dfs(self):
        pass

    def has_directed_cycle(self):
        pass


# Basic undirected graph tests
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('A', 'B')
g.add_edge('B', 'C')

g.print_graph()
print()

# Directed graph tests
g = Graph(directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('A', 'B')
g.add_edge('B', 'C')

g.print_graph()
print()


# Weighted graph tests
g = Graph(weighted=True, directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('A', 'B', 15)
g.add_edge('B', 'C', 34)

g.print_graph()

# Removal tests
print()
print("Removal test")
removal_test = Graph()
removal_test.add_vertex('A')
removal_test.add_vertex('B')
removal_test.add_vertex('C')

removal_test.add_edge('A', 'B')
removal_test.add_edge('B', 'C')

removal_test.print_graph()

removal_test.remove_edge('A', 'B')

removal_test.print_graph()

removal_test.remove_vertex('C')

removal_test.print_graph()
print()

# BFS tests
g.bfs('A')
g.bfs('B')
g.bfs('C')

g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

# More complex scenario to demonstrate BFS algorithm
g.add_edge('A', 'D')
g.add_edge('B', 'E')
g.add_edge('B', 'F')

g.bfs('A')


# DFS tests
g.add_vertex('G')
g.add_edge('F', 'G') # To demonstrate how DFS differs from BFS

g.dfs('A')
g.bfs('A')

# Why do these searching algorithms matter?
# DFS use case example: detecting cycles.
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')

print(g.has_undirected_cycle())