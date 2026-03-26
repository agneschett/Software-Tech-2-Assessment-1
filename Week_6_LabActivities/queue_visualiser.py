import tkinter as tk
from tkinter import messagebox
from collections import deque

NODE_WIDTH = 80
NODE_HEIGHT = 40
HORIZONTAL_GAP = 20
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 200

class QueueVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Visualizer (Deque)")

        self.queue = deque()

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack(pady=20)

        control_frame = tk.Frame(root)
        control_frame.pack()

        # Enqueue
        tk.Label(control_frame, text="Enqueue Value:").grid(row=0, column=0)
        self.enqueue_entry = tk.Entry(control_frame, width=10)
        self.enqueue_entry.grid(row=0, column=1)

        tk.Button(control_frame, text="Enqueue", command=self.enqueue_value).grid(row=0, column=2, padx=5)

        # Dequeue
        tk.Button(control_frame, text="Dequeue", command=self.dequeue_value).grid(row=1, column=2, pady=5)

        # Peek
        tk.Button(control_frame, text="Peek", command=self.peek_value).grid(row=2, column=2, pady=5)

        self.status_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.draw_queue()

    def draw_node(self, x, y, data):
        self.canvas.create_rectangle(x, y, x + NODE_WIDTH, y + NODE_HEIGHT,
                                     fill="lightgreen", outline="black", width=2)
        self.canvas.create_text(x + NODE_WIDTH/2, y + NODE_HEIGHT/2,
                                text=str(data), font=("Arial", 16))

    def draw_queue(self):
        self.canvas.delete("all")

        x = 20
        y = (CANVAS_HEIGHT - NODE_HEIGHT) // 2

        for i, val in enumerate(self.queue):
            self.draw_node(x, y, val)

            if i < len(self.queue) - 1:
                self.canvas.create_line(x + NODE_WIDTH, y + NODE_HEIGHT/2,
                                        x + NODE_WIDTH + HORIZONTAL_GAP, y + NODE_HEIGHT/2,
                                        arrow=tk.LAST, width=2)

            x += NODE_WIDTH + HORIZONTAL_GAP

        # Labels
        if self.queue:
            # Front
            self.canvas.create_text(40, y - 20, text="Front", fill="red", font=("Arial", 12))

            # Rear
            rear_x = 20 + (len(self.queue) - 1) * (NODE_WIDTH + HORIZONTAL_GAP)
            self.canvas.create_text(rear_x + NODE_WIDTH/2, y + NODE_HEIGHT + 20,
                                    text="Rear", fill="blue", font=("Arial", 12))

    # ------------------------
    # Queue Operations
    # ------------------------

    def enqueue_value(self):
        try:
            val = int(self.enqueue_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter an integer.")
            return

        self.queue.append(val)   # SAME as Task 2
        self.enqueue_entry.delete(0, tk.END)

        self.status_label.config(text=f"Enqueued {val}")
        self.draw_queue()

    def dequeue_value(self):
        if not self.queue:
            messagebox.showinfo("Empty Queue", "Queue is empty.")
            return

        val = self.queue.popleft()   # SAME as Task 2
        self.status_label.config(text=f"Dequeued {val}")
        self.draw_queue()

    def peek_value(self):
        if not self.queue:
            messagebox.showinfo("Empty Queue", "Queue is empty.")
            return

        val = self.queue[0]   # SAME as Task 2
        self.status_label.config(text=f"Front value is {val}")


# ------------------------
# Run App
# ------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueVisualizer(root)

    # Optional test
    # app.queue = deque([10, 20, 30])
    # app.draw_queue()

    root.mainloop()