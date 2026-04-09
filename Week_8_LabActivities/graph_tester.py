from graph import Graph
# Basic undirected graph tests
print("Basic undirected graph tests")
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('A', 'B')
g.add_edge('B', 'C')

g.print_graph()
print()

# Directed graph tests
print("Directed graph tests")
g = Graph(directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('A', 'B')
g.add_edge('B', 'C')

g.print_graph()
print()


# Weighted graph tests
print("Weighted graph tests")
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

# BFS on the graph from Activity 1
print("BFS starting from vertex 'A':")
visited_bfs = g.bfs('A')
print("Visited vertices in BFS order:", visited_bfs)


# DFS on the same graph
print() 
print("DFS starting from vertex 'A':")
visited_dfs = g.dfs('A')
print("Visited vertices in DFS order:", visited_dfs)

#cycle detection in undirected graphs
# Create graph with a cycle
print()
cycle_graph = Graph(directed=False)
for v in ['A', 'B', 'C']:
    cycle_graph.add_vertex(v)
cycle_graph.add_edge('A', 'B')
cycle_graph.add_edge('B', 'C')
cycle_graph.add_edge('C', 'A') # Closing the cycle
print("Does cycle_graph have a cycle? ",
cycle_graph.has_undirected_cycle())


# Create graph without a cycle
print()
acyclic_graph = Graph(directed=False)
for v in ['X', 'Y', 'Z']:
    acyclic_graph.add_vertex(v)
acyclic_graph.add_edge('X', 'Y')
acyclic_graph.add_edge('Y', 'Z')
print("Does acyclic_graph have a cycle? ",
acyclic_graph.has_undirected_cycle())

# Create weighted directed graph
print()
wg = Graph(directed=True, weighted=True)
for v in ['A', 'B', 'C']:
    wg.add_vertex(v)
wg.add_edge('A', 'B', weight=15)
wg.add_edge('B', 'C', weight=34)
wg.add_edge('A', 'C', weight=50)
print("Weighted Directed Graph:")
wg.print_graph()