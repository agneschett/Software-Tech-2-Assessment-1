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
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return True

        current = self.head
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1
        
        if count == index:
            new_node.next = current
            new_node.prev = prev
            prev.next = new_node
            if current:
                current.prev = new_node
            return True
        else:
            return False

    def delete_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:   # deleting head
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
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

class DoublyLinkedListVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Doubly Linked List Visualizer")

        self.dll = DoublyLinkedList()

        # UI Setup
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack(pady=20)

        control_frame = tk.Frame(root)
        control_frame.pack()

        # Insert controls
        tk.Label(control_frame, text="Insert Value:").grid(row=0, column=0)
        self.insert_value_entry = tk.Entry(control_frame, width=5)
        self.insert_value_entry.grid(row=0, column=1)

        tk.Label(control_frame, text="at Index:").grid(row=0, column=2)
        self.insert_index_entry = tk.Entry(control_frame, width=5)
        self.insert_index_entry.grid(row=0, column=3)

        insert_btn = tk.Button(control_frame, text="Insert", command=self.insert_node)
        insert_btn.grid(row=0, column=4, padx=10)

        # Delete controls
        tk.Label(control_frame, text="Delete Value:").grid(row=1, column=0)
        self.delete_value_entry = tk.Entry(control_frame, width=5)
        self.delete_value_entry.grid(row=1, column=1)
        delete_btn = tk.Button(control_frame, text="Delete", command=self.delete_node)
        delete_btn.grid(row=1, column=4, padx=10)

        # Search controls
        tk.Label(control_frame, text="Search Value:").grid(row=2, column=0)
        self.search_value_entry = tk.Entry(control_frame, width=5)
        self.search_value_entry.grid(row=2, column=1)
        search_btn = tk.Button(control_frame, text="Search", command=self.search_node)
        search_btn.grid(row=2, column=4, padx=10)

        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.status_label.pack(pady=10)

        self.draw_list()

    def draw_node(self, x, y, data, highlight=False):
        fill_color = "yellow" if highlight else "lightgrey"
        outline_color = "red" if highlight else "black"

        # Draw rectangle for node
        self.canvas.create_rectangle(x, y, x + NODE_WIDTH, y + NODE_HEIGHT,
                                     fill=fill_color, outline=outline_color, width=2)
        # Draw value text centered
        self.canvas.create_text(x + NODE_WIDTH // 2, y + NODE_HEIGHT // 2,
                                text=str(data), font=("Arial", 16))

    def draw_arrow(self, x1, y1, x2, y2):
        # Draw simple arrow line with arrowhead at (x2,y2)
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, width=2)

    def draw_double_arrow(self, x1, y1, x2, y2):
        # Draw two arrows pointing opposite directions between x1,y1 and x2,y2
        self.canvas.create_line(x1, y1, x2, y2, arrow=tk.BOTH, width=2)

    def draw_list(self, highlight_index=None):
        self.canvas.delete("all")
        nodes = self.dll.to_list()
        x = 20
        y = 40

        # Keep coordinates of centers to draw arrows between nodes
        centers = []

        # Draw nodes
        for i, val in enumerate(nodes):
            highlight = (i == highlight_index)
            self.draw_node(x, y, val, highlight)
            centers.append((x + NODE_WIDTH // 2, y + NODE_HEIGHT // 2))
            x += NODE_WIDTH + HORIZONTAL_GAP

        # Draw arrows (both ways)
        for i in range(len(centers) - 1):
            x1, y1 = centers[i]
            x2, y2 = centers[i + 1]
            # Arrow from node i to i+1 (forward)
            self.draw_arrow(x1 + 15, y1, x2 - 15, y2)
            # Arrow from node i+1 to i (backward)
            self.draw_arrow(x2 - 15, y2 + 10, x1 + 15, y1 + 10)

    def insert_node(self):
        try:
            val = int(self.insert_value_entry.get())
            index = int(self.insert_index_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for value and index.")
            return
        if index < 0:
            messagebox.showerror("Input Error", "Index must be non-negative.")
            return
        success = self.dll.insert_at_index(val, index)
        if not success:
            messagebox.showerror("Index Error", "Index out of range.")
            return
        self.status_label.config(text=f"Inserted {val} at index {index}")
        self.draw_list()

    def delete_node(self):
        try:
            val = int(self.delete_value_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer value to delete.")
            return
        success = self.dll.delete_value(val)
        if success:
            self.status_label.config(text=f"Deleted value {val} from the list")
            self.draw_list()
        else:
            messagebox.showinfo("Not Found", f"Value {val} not found.")

    def search_node(self):
        try:
            val = int(self.search_value_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer value to search.")
            return

        nodes = self.dll.to_list()
        found_index = -1

        def highlight_next(i=0):
            if i > 0:
                self.draw_list()
            if i < len(nodes):
                self.draw_list(highlight_index=i)
                if nodes[i] == val:
                    self.status_label.config(text=f"Value {val} found at index {i}")
                    return
                self.root.after(500, lambda: highlight_next(i + 1))
            else:
                self.status_label.config(text=f"Value {val} not found in the list")
                self.draw_list()

        highlight_next()

if __name__ == "__main__":
    root = tk.Tk()
    app = DoublyLinkedListVisualizer(root)

    # Optional: Pre-populate list
    for v in [10, 20, 30, 40]:
        app.dll.insert_at_index(v, app.dll.search(v)+1 if app.dll.search(v) != -1 else 100)  # Insert at end
    app.draw_list()

    root.mainloop()
