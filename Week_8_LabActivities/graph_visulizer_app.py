import tkinter as tk
import math
import time
import threading
from collections import defaultdict


# ===== GRAPH CLASS =====
class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = defaultdict(list)
        self.weights = {}
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2, weight=0):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            if self.weighted:
                self.weights[(v1, v2)] = weight

            if not self.directed:
                self.graph[v2].append(v1)
                if self.weighted:
                    self.weights[(v2, v1)] = weight


# ===== GRAPH VISUALIZER =====
class GraphVisualizer(tk.Tk):
    def __init__(self, graph):
        super().__init__()
        self.title("Graph Visualizer")
        self.geometry('650x650')

        self.graph = graph

        self.canvas = tk.Canvas(self, width=600, height=600, bg='white')
        self.canvas.pack(pady=10)

        self.vertex_positions = {}
        self.vertex_circles = {}
        self.edge_lines = {}

        self.node_radius = 20
        self.spacing = 180
        self.center = (300, 300)

        # Buttons
        control_frame = tk.Frame(self)
        control_frame.pack()

        tk.Button(control_frame, text="Run BFS",
                  command=lambda: self.run_traversal("bfs")).pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="Run DFS",
                  command=lambda: self.run_traversal("dfs")).pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="Detect Undirected Cycle",
                  command=self.run_cycle_detection).pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="Detect Directed Cycle",
                  command=self.run_directed_cycle_detection).pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="Reset Colors",
                  command=self.reset_colors).pack(side=tk.LEFT, padx=5)

        self.info_label = tk.Label(self, text="")
        self.info_label.pack(pady=5)

        self.draw_graph()

    # ===== DRAW GRAPH =====
    def draw_graph(self):
        self.canvas.delete("all")
        self.vertex_positions.clear()
        self.vertex_circles.clear()
        self.edge_lines.clear()

        vertices = list(self.graph.graph.keys())
        n = len(vertices)
        if n == 0:
            return

        angle_gap = 360 / n
        cx, cy = self.center

        # Draw vertices
        for i, v in enumerate(vertices):
            angle = i * angle_gap
            x = cx + self.spacing * math.cos(math.radians(angle))
            y = cy + self.spacing * math.sin(math.radians(angle))

            self.vertex_positions[v] = (x, y)

            circle = self.canvas.create_oval(
                x - self.node_radius, y - self.node_radius,
                x + self.node_radius, y + self.node_radius,
                fill='lightblue', outline='black', width=2
            )

            self.vertex_circles[v] = circle
            self.canvas.create_text(x, y, text=v, font=("Arial", 12, "bold"))

        # Draw edges
        for v in vertices:
            x1, y1 = self.vertex_positions[v]

            for nbr in self.graph.graph[v]:
                x2, y2 = self.vertex_positions[nbr]

                dx, dy = x2 - x1, y2 - y1
                dist = math.sqrt(dx * dx + dy * dy)
                if dist == 0:
                    continue

                offset_x = dx / dist * self.node_radius
                offset_y = dy / dist * self.node_radius

                start = (x1 + offset_x, y1 + offset_y)
                end = (x2 - offset_x, y2 - offset_y)

                if self.graph.directed:
                    line = self.canvas.create_line(*start, *end, arrow=tk.LAST, width=2)
                else:
                    line = self.canvas.create_line(*start, *end, width=2)

                self.edge_lines[(v, nbr)] = line

    # ===== RESET =====
    def reset_colors(self):
        for circle in self.vertex_circles.values():
            self.canvas.itemconfig(circle, fill='lightblue')

        for edge in self.edge_lines.values():
            self.canvas.itemconfig(edge, fill='black', width=2)

        self.info_label.config(text="")

    # ===== HIGHLIGHT =====
    def highlight_vertex(self, v, color):
        if v in self.vertex_circles:
            self.canvas.itemconfig(self.vertex_circles[v], fill=color)
            self.update()

    def highlight_edge(self, v1, v2, color):
        if (v1, v2) in self.edge_lines:
            self.canvas.itemconfig(self.edge_lines[(v1, v2)], fill=color, width=3)
            self.update()

    # ===== BFS / DFS =====
    def run_traversal(self, method):
        def worker():
            self.reset_colors()
            visited = set()

            start = next(iter(self.graph.graph), None)
            if not start:
                return

            if method == "bfs":
                queue = [start]
                self.info_label.config(text="Running BFS...")

                while queue:
                    v = queue.pop(0)
                    if v not in visited:
                        self.highlight_vertex(v, 'orange')
                        visited.add(v)
                        time.sleep(0.7)

                        for nbr in self.graph.graph[v]:
                            if nbr not in visited:
                                queue.append(nbr)
                                self.highlight_edge(v, nbr, 'green')
                                time.sleep(0.3)

                self.info_label.config(text="BFS complete")

            else:  # DFS
                stack = [start]
                self.info_label.config(text="Running DFS...")

                while stack:
                    v = stack.pop()
                    if v not in visited:
                        self.highlight_vertex(v, 'purple')
                        visited.add(v)
                        time.sleep(0.7)

                        for nbr in reversed(self.graph.graph[v]):
                            if nbr not in visited:
                                stack.append(nbr)
                                self.highlight_edge(v, nbr, 'blue')
                                time.sleep(0.3)

                self.info_label.config(text="DFS complete")

        threading.Thread(target=worker, daemon=True).start()

    # ===== UNDIRECTED CYCLE =====
    def run_cycle_detection(self):
        def worker():
            self.reset_colors()

            if self.graph.directed:
                self.info_label.config(text="Only for undirected graphs")
                return

            visited = set()

            def dfs(v, parent):
                visited.add(v)
                self.highlight_vertex(v, 'yellow')
                time.sleep(0.5)

                for nbr in self.graph.graph[v]:
                    if nbr not in visited:
                        self.highlight_edge(v, nbr, 'orange')
                        time.sleep(0.4)
                        if dfs(nbr, v):
                            return True
                    elif nbr != parent:
                        self.highlight_edge(v, nbr, 'red')
                        self.highlight_vertex(v, 'red')
                        self.highlight_vertex(nbr, 'red')
                        return True
                return False

            for v in self.graph.graph:
                if v not in visited:
                    if dfs(v, None):
                        self.info_label.config(text="Cycle detected!")
                        return

            self.info_label.config(text="No cycle found")

        threading.Thread(target=worker, daemon=True).start()

    # ===== DIRECTED CYCLE =====
    def run_directed_cycle_detection(self):
        def worker():
            self.reset_colors()

            if not self.graph.directed:
                self.info_label.config(text="Only for directed graphs")
                return

            visited = set()
            rec_stack = set()

            def dfs(v):
                visited.add(v)
                rec_stack.add(v)
                self.highlight_vertex(v, 'yellow')
                time.sleep(0.5)

                for nbr in self.graph.graph[v]:
                    if nbr not in visited:
                        self.highlight_edge(v, nbr, 'orange')
                        time.sleep(0.4)
                        if dfs(nbr):
                            return True
                    elif nbr in rec_stack:
                        self.highlight_edge(v, nbr, 'red')
                        self.highlight_vertex(v, 'red')
                        self.highlight_vertex(nbr, 'red')
                        return True

                rec_stack.remove(v)
                return False

            for v in self.graph.graph:
                if v not in visited:
                    if dfs(v):
                        self.info_label.config(text="Directed cycle detected!")
                        return

            self.info_label.config(text="No directed cycle")

        threading.Thread(target=worker, daemon=True).start()


# ===== MAIN =====
if __name__ == "__main__":
    g = Graph(directed=True)

    for v in ['A', 'B', 'C', 'D']:
        g.add_vertex(v)

    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')  # cycle
    g.add_edge('C', 'D')

    app = GraphVisualizer(g)
    app.mainloop()
