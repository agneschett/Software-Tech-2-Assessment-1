import tkinter as tk
from tkinter import messagebox

# ===== RED-BLACK TREE =====
class RBNode:
    def __init__(self, name, phone, color="red"):
        self.name = name
        self.phone = phone
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, None, "black")
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, name, phone):
        node = RBNode(name, phone)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            current = current.left if node.name < current.name else current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.name < parent.name:
            parent.left = node
        else:
            parent.right = node

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent and k.parent.color == "red":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "red":
                    k.parent.color = "black"
                    u.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "red":
                    k.parent.color = "black"
                    u.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
        self.root.color = "black"

    def search(self, node, name):
        while node != self.NIL and name != node.name:
            node = node.left if name < node.name else node.right
        return node if node != self.NIL else None

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, name):
        z = self.search(self.root, name)
        if z is None:
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "black":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"


# ===== GUI =====
class RBTVisualizer:
    def __init__(self, master):
        self.master = master
        master.title("Red-Black Tree Visualiser")

        self.rbt = RedBlackTree()

        # Input
        frame = tk.Frame(master)
        frame.pack(pady=10)
        tk.Label(frame, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1)
        tk.Label(frame, text="Phone:").grid(row=1, column=0)
        self.phone_entry = tk.Entry(frame)
        self.phone_entry.grid(row=1, column=1)

        # Buttons
        tk.Button(frame, text="Insert", command=self.insert).grid(row=2, column=0, pady=5)
        tk.Button(frame, text="Delete", command=self.delete).grid(row=2, column=1)
        tk.Button(frame, text="Search", command=self.search).grid(row=2, column=2)

        # Output
        self.output = tk.Text(master, height=5, width=60)
        self.output.pack()

        # Canvas
        self.canvas = tk.Canvas(master, width=900, height=400, bg="white")
        self.canvas.pack(pady=10)

    def insert(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if not name or not phone:
            return
        self.rbt.insert(name, phone)
        self.draw_tree()

    def delete(self):
        name = self.name_entry.get().strip()
        if not name:
            return
        self.rbt.delete(name)
        self.draw_tree()

    def search(self):
        name = self.name_entry.get().strip()
        node = self.rbt.search(self.rbt.root, name)
        self.output.delete(1.0, tk.END)
        if node:
            self.output.insert(tk.END, f"Found: {node.name}, Phone: {node.phone}")
        else:
            self.output.insert(tk.END, "Not found")

    def draw_tree(self):
        self.canvas.delete("all")
        self._draw_node(self.rbt.root, 450, 20, 200)

    def _draw_node(self, node, x, y, offset):
        if node is None or node.name is None:
            return
        radius = 20
        if node.left and node.left.name is not None:
            x_left = x - offset
            y_left = y + 70
            self.canvas.create_line(x, y, x_left, y_left)
            self._draw_node(node.left, x_left, y_left, offset // 2)
        if node.right and node.right.name is not None:
            x_right = x + offset
            y_right = y + 70
            self.canvas.create_line(x, y, x_right, y_right)
            self._draw_node(node.right, x_right, y_right, offset // 2)
        color = "red" if node.color == "red" else "black"
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
        self.canvas.create_text(x, y, text=node.name[:5], fill="white" if color=="black" else "black")


# ===== RUN =====
if __name__ == "__main__":
    root = tk.Tk()
    app = RBTVisualizer(root)
    root.mainloop()