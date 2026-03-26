import tkinter as tk
from tkinter import messagebox

NODE_WIDTH = 60
NODE_HEIGHT = 40
HORIZONTAL_GAP = 40
CANVAS_HEIGHT = 120
CANVAS_WIDTH = 900


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, data, index):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return True

        current = self.head
        prev = None
        count = 0

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if count == index:
            prev.next = new_node
            new_node.next = current
            return True
        return False

    def delete_value(self, value):
        current = self.head
        prev = None

        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search(self, value):
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def to_list(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr


# ---------------------------
# Visualiser
# ---------------------------

class SinglyLinkedListVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Singly Linked List Visualizer")

        self.sll = SinglyLinkedList()

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack(pady=20)

        control_frame = tk.Frame(root)
        control_frame.pack()

        # Insert
        tk.Label(control_frame, text="Insert Value:").grid(row=0, column=0)
        self.insert_value_entry = tk.Entry(control_frame, width=5)
        self.insert_value_entry.grid(row=0, column=1)

        tk.Label(control_frame, text="at Index:").grid(row=0, column=2)
        self.insert_index_entry = tk.Entry(control_frame, width=5)
        self.insert_index_entry.grid(row=0, column=3)

        tk.Button(control_frame, text="Insert", command=self.insert_node).grid(row=0, column=4, padx=10)

        # Delete
        tk.Label(control_frame, text="Delete Value:").grid(row=1, column=0)
        self.delete_value_entry = tk.Entry(control_frame, width=5)
        self.delete_value_entry.grid(row=1, column=1)

        tk.Button(control_frame, text="Delete", command=self.delete_node).grid(row=1, column=4, padx=10)

        # Search
        tk.Label(control_frame, text="Search Value:").grid(row=2, column=0)
        self.search_value_entry = tk.Entry(control_frame, width=5)
        self.search_value_entry.grid(row=2, column=1)

        tk.Button(control_frame, text="Search", command=self.search_node).grid(row=2, column=4, padx=10)

        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.status_label.pack(pady=10)

        self.draw_list()

    def draw_node(self, x, y, data, highlight=False):
        fill = "yellow" if highlight else "lightgrey"
        outline = "red" if highlight else "black"

        self.canvas.create_rectangle(x, y, x + NODE_WIDTH, y + NODE_HEIGHT,
                                     fill=fill, outline=outline, width=2)

        self.canvas.create_text(x + NODE_WIDTH // 2, y + NODE_HEIGHT // 2,
                                text=str(data), font=("Arial", 16))

    def draw_arrow(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, width=2)

    def draw_list(self, highlight_index=None):
        self.canvas.delete("all")

        nodes = self.sll.to_list()
        x = 20
        y = 40

        centers = []

        # Draw nodes
        for i, val in enumerate(nodes):
            self.draw_node(x, y, val, highlight=(i == highlight_index))
            centers.append((x + NODE_WIDTH // 2, y + NODE_HEIGHT // 2))
            x += NODE_WIDTH + HORIZONTAL_GAP

        # Draw ONLY forward arrows
        for i in range(len(centers) - 1):
            x1, y1 = centers[i]
            x2, y2 = centers[i + 1]
            self.draw_arrow(x1 + 15, y1, x2 - 15, y2)

    def insert_node(self):
        try:
            val = int(self.insert_value_entry.get())
            index = int(self.insert_index_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid integers")
            return

        if index < 0:
            messagebox.showerror("Error", "Index must be non-negative")
            return

        if self.sll.insert_at_index(val, index):
            self.status_label.config(text=f"Inserted {val} at index {index}")
            self.draw_list()
        else:
            messagebox.showerror("Error", "Index out of range")

    def delete_node(self):
        try:
            val = int(self.delete_value_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid integer")
            return

        if self.sll.delete_value(val):
            self.status_label.config(text=f"Deleted {val}")
            self.draw_list()
        else:
            messagebox.showinfo("Not Found", f"{val} not found")

    def search_node(self):
        try:
            val = int(self.search_value_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid integer")
            return

        nodes = self.sll.to_list()

        def animate(i=0):
            if i > 0:
                self.draw_list()

            if i < len(nodes):
                self.draw_list(highlight_index=i)

                if nodes[i] == val:
                    self.status_label.config(text=f"Found {val} at index {i}")
                    return

                self.root.after(500, lambda: animate(i + 1))
            else:
                self.status_label.config(text=f"{val} not found")

        animate()


# ---------------------------
# Run App
# ---------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = SinglyLinkedListVisualizer(root)

    # Preload values
    for v in [10, 20, 30, 40]:
        app.sll.insert_at_index(v, 100)

    app.draw_list()
    root.mainloop()