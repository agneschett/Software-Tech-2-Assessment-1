import tkinter as tk
from tkinter import messagebox
import heapq

NODE_WIDTH = 60
NODE_HEIGHT = 40
HORIZONTAL_GAP = 10
VERTICAL_GAP = 50
CANVAS_WIDTH = 700
CANVAS_HEIGHT = 400

class PriorityQueueVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Priority Queue Visualizer")

        self.heap = []

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack(pady=20)

        control_frame = tk.Frame(root)
        control_frame.pack()

        tk.Label(control_frame, text="Add Task (priority,value):").grid(row=0, column=0)
        self.task_entry = tk.Entry(control_frame, width=20)
        self.task_entry.grid(row=0, column=1)

        add_btn = tk.Button(control_frame, text="Add Task", command=self.add_task)
        add_btn.grid(row=0, column=2, padx=5)

        pop_btn = tk.Button(control_frame, text="Pop Task", command=self.pop_task)
        pop_btn.grid(row=1, column=2, pady=5)

        self.status_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.draw_heap()

    def draw_node(self, x, y, val):
        rect = self.canvas.create_rectangle(x, y, x + NODE_WIDTH, y + NODE_HEIGHT,
                                            fill="orange", outline="black", width=2)
        self.canvas.create_text(x + NODE_WIDTH/2, y + NODE_HEIGHT/2, text=str(val), font=("Arial", 14))
        return rect

    def draw_lines(self, x1, y1, x2, y2):
        self.canvas.create_line(x1 + NODE_WIDTH/2, y1 + NODE_HEIGHT, x2 + NODE_WIDTH/2, y2, width=2)

    def draw_heap(self):
        self.canvas.delete("all")
        if not self.heap:
            return
        # Draw nodes in tree-like structure
        level_indices = [0]
        level = 0
        y = 20
        # Calculate positions
        positions = {}
        width = CANVAS_WIDTH

        def calc_x(i, level):
            gaps = 2 ** (level + 1)
            pos = (i * width) // gaps + width // (2 * gaps)
            return pos

        i = 0
        while i < len(self.heap):
            nodes_this_level = 2 ** level
            for j in range(nodes_this_level):
                if i >= len(self.heap):
                    break
                x = calc_x(j, level)
                positions[i] = (x, y)
                i += 1
            y += VERTICAL_GAP
            level += 1

        # Draw lines (parent->child)
        for i in range(len(self.heap)):
            left = 2*i + 1
            right = 2*i + 2
            if left < len(self.heap):
                x1, y1 = positions[i]
                x2, y2 = positions[left]
                self.draw_lines(x1, y1, x2, y2)
            if right < len(self.heap):
                x1, y1 = positions[i]
                x2, y2 = positions[right]
                self.draw_lines(x1, y1, x2, y2)

        # Draw nodes
        for i, val in enumerate(self.heap):
            x, y = positions[i]
            self.draw_node(x, y, val)

    def add_task(self):
        val = self.task_entry.get()
        try:
            # Expect input as "priority,value"
            prio_str, task_val = val.split(',')
            prio = int(prio_str.strip())
            task_val = task_val.strip()
        except Exception:
            messagebox.showerror("Input Error", "Input should be in 'priority,value' format. Example: 2,TaskA")
            return
        heapq.heappush(self.heap, (prio, task_val))
        self.task_entry.delete(0, tk.END)
        self.status_label.config(text=f"Added task '{task_val}' with priority {prio}")
        self.draw_heap()

    def pop_task(self):
        if not self.heap:
            messagebox.showinfo("Empty Queue", "No tasks available to pop.")
            return
        prio, task = heapq.heappop(self.heap)
        self.status_label.config(text=f"Popped task '{task}' with priority {prio}")
        self.draw_heap()

if __name__ == "__main__":
    root = tk.Tk()
    app = PriorityQueueVisualizer(root)

    # Example test cases:
    # heapq.heappush(app.heap, (1,"Eat"))
    # heapq.heappush(app.heap, (3,"Sleep"))
    # heapq.heappush(app.heap, (2,"Work"))
    # app.draw_heap()

    root.mainloop()
