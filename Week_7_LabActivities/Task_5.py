import time
import random
import string
import tkinter as tk
from tkinter import ttk


# ===== BST =====
class Node:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, name, phone):
        if root is None:
            return Node(name, phone)
        if name < root.name:
            root.left = self.insert(root.left, name, phone)
        elif name > root.name:
            root.right = self.insert(root.right, name, phone)
        else:
            root.phone = phone
        return root

    def search(self, root, name):
        if root is None or root.name == name:
            return root
        if name < root.name:
            return self.search(root.left, name)
        return self.search(root.right, name)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, name):
        if root is None:
            return root

        if name < root.name:
            root.left = self.delete(root.left, name)
        elif name > root.name:
            root.right = self.delete(root.right, name)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.name = temp.name
            root.phone = temp.phone
            root.right = self.delete(root.right, temp.name)

        return root


# ===== AVL =====
class AVLNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, node, name, phone):
        if not node:
            return AVLNode(name, phone)

        if name < node.name:
            node.left = self.insert(node.left, name, phone)
        elif name > node.name:
            node.right = self.insert(node.right, name, phone)
        else:
            node.phone = phone
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and name < node.left.name:
            return self.right_rotate(node)
        if balance < -1 and name > node.right.name:
            return self.left_rotate(node)
        if balance > 1 and name > node.left.name:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and name < node.right.name:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, name):
        if not root:
            return root

        if name < root.name:
            root.left = self.delete(root.left, name)
        elif name > root.name:
            root.right = self.delete(root.right, name)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.name = temp.name
            root.phone = temp.phone
            root.right = self.delete(root.right, temp.name)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, node, name):
        if node is None or node.name == name:
            return node
        if name < node.name:
            return self.search(node.left, name)
        return self.search(node.right, name)


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
            if node.name < current.name:
                current = current.left
            else:
                current = current.right

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

# ===== TREE VISUALISER GUI =====
class TreeVisualizer:
    def __init__(self, master):
        self.master = master
        master.title("Tree Visualiser (BST vs AVL vs RBT)")

        # Trees
        self.bst = BST()
        self.avl = AVLTree()
        self.rbt = RedBlackTree()

        self.current_tree = "AVL"

        # ===== Controls =====
        control_frame = tk.Frame(master)
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(control_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(control_frame, text="Phone").grid(row=1, column=0)
        self.phone_entry = tk.Entry(control_frame)
        self.phone_entry.grid(row=1, column=1)

        # Tree selector
        self.tree_type = tk.StringVar(value="AVL")
        tk.OptionMenu(control_frame, self.tree_type, "BST", "AVL", "RBT").grid(row=0, column=2, padx=10)

        # Buttons
        tk.Button(control_frame, text="Insert", command=self.insert).grid(row=2, column=0, pady=5)
        tk.Button(control_frame, text="Delete", command=self.delete).grid(row=2, column=1)
        tk.Button(control_frame, text="Search", command=self.search).grid(row=2, column=2)

        # Output
        self.output = tk.Text(master, height=5, width=60)
        self.output.pack()

        # Canvas
        self.canvas = tk.Canvas(master, width=900, height=400, bg="white")
        self.canvas.pack(pady=10)

    # ===== OPERATIONS =====
    def insert(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        tree = self.tree_type.get()

        if tree == "BST":
            self.bst.root = self.bst.insert(self.bst.root, name, phone)
        elif tree == "AVL":
            self.avl.root = self.avl.insert(self.avl.root, name, phone)
        else:
            self.rbt.insert(name, phone)

        self.draw()

    def delete(self):
        name = self.name_entry.get()
        tree = self.tree_type.get()

        if tree == "BST":
            self.bst.root = self.bst.delete(self.bst.root, name)
        elif tree == "AVL":
            self.avl.root = self.avl.delete(self.avl.root, name)

        self.draw()

    def search(self):
        name = self.name_entry.get()
        tree = self.tree_type.get()

        if tree == "BST":
            result = self.bst.search(self.bst.root, name)
        elif tree == "AVL":
            result = self.avl.search(self.avl.root, name)
        else:
            result = self.rbt.search(self.rbt.root, name)

        self.output.delete(1.0, tk.END)
        if result:
            self.output.insert(tk.END, f"Found: {name}")
        else:
            self.output.insert(tk.END, "Not found")

    # ===== DRAW TREE =====
    def draw(self):
        self.canvas.delete("all")

        tree = self.tree_type.get()

        if tree == "BST":
            self._draw_node(self.bst.root, 450, 20, 200, "BST")
        elif tree == "AVL":
            self._draw_node(self.avl.root, 450, 20, 200, "AVL")
        else:
            self._draw_node(self.rbt.root, 450, 20, 200, "RBT")

    def _draw_node(self, node, x, y, offset, tree_type):
        if not node or (tree_type == "RBT" and node == self.rbt.NIL):
            return

        radius = 20

        # LEFT
        if node.left:
            if not (tree_type == "RBT" and node.left == self.rbt.NIL):
                x_left = x - offset
                y_left = y + 70
                self.canvas.create_line(x, y, x_left, y_left)
                self._draw_node(node.left, x_left, y_left, offset // 2, tree_type)

        # RIGHT
        if node.right:
            if not (tree_type == "RBT" and node.right == self.rbt.NIL):
                x_right = x + offset
                y_right = y + 70
                self.canvas.create_line(x, y, x_right, y_right)
                self._draw_node(node.right, x_right, y_right, offset // 2, tree_type)

        # COLOR
        if tree_type == "RBT":
            color = "red" if node.color == "red" else "black"
            text_color = "white"
        else:
            color = "lightgreen"
            text_color = "black"

        # DRAW NODE
        self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=color
        )

        self.canvas.create_text(
            x, y,
            text=node.name[:5],
            fill=text_color
        )

# ===== BENCHMARK =====
def benchmark(n=10000):
    names = [''.join(random.choices(string.ascii_lowercase, k=10)) for _ in range(n)]
    phones = [''.join(random.choices(string.digits, k=10)) for _ in range(n)]

    # BST
    bst = BST()
    start = time.time()
    for i in range(n):
        bst.root = bst.insert(bst.root, names[i], phones[i])
    bst_insert = time.time() - start

    # AVL
    avl = AVLTree()
    start = time.time()
    for i in range(n):
        avl.root = avl.insert(avl.root, names[i], phones[i])
    avl_insert = time.time() - start

    # RBT
    rbt = RedBlackTree()
    start = time.time()
    for i in range(n):
        rbt.insert(names[i], phones[i])
    rbt_insert = time.time() - start

    # SEARCH
    sample = random.sample(names, n // 2)

    start = time.time()
    for name in sample:
        bst.search(bst.root, name)
    bst_search = time.time() - start

    start = time.time()
    for name in sample:
        avl.search(avl.root, name)
    avl_search = time.time() - start

    start = time.time()
    for name in sample:
        rbt.search(rbt.root, name)
    rbt_search = time.time() - start

    return {
        "Insertions": (bst_insert, avl_insert, rbt_insert),
        "Searches": (bst_search, avl_search, rbt_search),
        "Deletions": (0, 0, 0)
    }


# ===== GUI =====
class BenchmarkApp:
    def __init__(self, root):
        root.title("BST vs AVL vs RBT")

        tk.Button(root, text="Run Benchmark", command=self.run).pack(pady=10)

        self.text = tk.Text(root, height=8, width=70)
        self.text.pack()

        self.tree = ttk.Treeview(root, columns=("BST", "AVL", "RBT"), show="headings")
        for col in ("BST", "AVL", "RBT"):
            self.tree.heading(col, text=col)
        self.tree.pack()

    def run(self):
        self.text.delete(1.0, tk.END)
        results = benchmark()

        summary = (
            f"Insertion → BST {results['Insertions'][0]:.4f}s | AVL {results['Insertions'][1]:.4f}s | RBT {results['Insertions'][2]:.4f}s\n"
            f"Search → BST {results['Searches'][0]:.4f}s | AVL {results['Searches'][1]:.4f}s | RBT {results['Searches'][2]:.4f}s\n"
        )
        self.text.insert(tk.END, summary)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for op in results:
            bst, avl, rbt = results[op]
            self.tree.insert("", tk.END, values=(f"{bst:.4f}", f"{avl:.4f}", f"{rbt:.4f}"))


# ===== RUN =====
if __name__ == "__main__":
    root = tk.Tk()

    # Choose ONE to run
    # app = BenchmarkApp(root)
    app = TreeVisualizer(root)

    root.mainloop()