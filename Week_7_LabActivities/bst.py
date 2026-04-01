class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Example: create root node
root = Node(10)
root.left = Node(5)
root.right = Node(15)

def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def search_bst(root, val):
    if root is None or root.value == val:
        return root
    if val < root.value:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)
    
def insert_bst(root, val):
    if root is None:
        return Node(val)
    if val < root.value:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current

def delete_node(root, val):
    if root is None:
        return root
    if val < root.value:
        root.left = delete_node(root.left, val)
    elif val > root.value:
        root.right = delete_node(root.right, val)
    else:
        # Node with 1 or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    return root

from collections import deque
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None

class ContactDirectory:
    def __init__(self):
        self.root = None

    def insert(self, root, name, phone):
        if root is None:
            return Contact(name, phone)
        if name < root.name:
            root.left = self.insert(root.left, name, phone)
        elif name > root.name:
            root.right = self.insert(root.right, name, phone)
        else:
            # Update phone if contact already exists
            root.phone = phone
        return root

    def search(self, root, name):
        if root is None or root.name == name:
            return root
        if name < root.name:
            return self.search(root.left, name)
        else:
            return self.search(root.right, name)

    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current

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
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.name = temp.name
            root.phone = temp.phone
            root.right = self.delete(root.right, temp.name)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Name: {root.name}, Phone: {root.phone}")
            self.inorder(root.right)

# # Testing the binary search tree (
# directory = ContactDirectory()
# directory.root = directory.insert(directory.root, 'Alice', '123-456-7890')
# directory.root = directory.insert(directory.root, 'Bob', '234-567-8901')
# directory.root = directory.insert(directory.root, 'Eve', '345-678-9012')

# print("All contacts:")
# directory.inorder(directory.root)

# print("\nSearching for Bob:")
# contact = directory.search(directory.root, 'Bob')
# if contact:
#     print(f"Found contact: {contact.name} - {contact.phone}")
# else:
#     print("Contact not found")

# print("\nDeleting Alice:")
# directory.root = directory.delete(directory.root, 'Alice')
# directory.inorder(directory.root)

import tkinter as tk
from tkinter import messagebox
import time
import random
import string


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None


class ContactDirectory:
    def __init__(self):
        self.root = None

    def insert(self, root, name, phone):
        if root is None:
            return Contact(name, phone)
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
        else:
            return self.search(root.right, name)

    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current

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
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.name = temp.name
            root.phone = temp.phone
            root.right = self.delete(root.right, temp.name)
        return root

    def inorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.inorder(root.left, result)
            result.append((root.name, root.phone))
            self.inorder(root.right, result)
        return result


# ---- Tkinter GUI ----
class BSTVisualizerApp:
    def __init__(self, root):
        self.directory = ContactDirectory()
        self.root = root
        self.root.title("Contact Directory BST")

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Phone:").grid(row=1, column=0, padx=5)
        self.phone_entry = tk.Entry(frame)
        self.phone_entry.grid(row=1, column=1, padx=5)

        button_frame = tk.Frame(root)
        button_frame.pack()

        self.insert_btn = tk.Button(button_frame, text="Insert Contact", command=self.insert_contact)
        self.insert_btn.grid(row=0, column=0, padx=5)

        self.search_btn = tk.Button(button_frame, text="Search Contact", command=self.search_contact)
        self.search_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_btn.grid(row=0, column=2, padx=5)

        self.show_all_btn = tk.Button(button_frame, text="Show All Contacts", command=self.show_all)
        self.show_all_btn.grid(row=0, column=3, padx=5)

        self.benchmark_btn = tk.Button(button_frame, text="Run Benchmark", command=self.benchmark)
        self.benchmark_btn.grid(row=0, column=4, padx=5)

        self.output_text = tk.Text(root, height=10, width=60)
        self.output_text.pack(pady=10)

        self.canvas = tk.Canvas(root, width=800, height=400, bg='white')
        self.canvas.pack(pady=10)

    # ---- GUI Functions ----
    def insert_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Please enter both name and phone number.")
            return

        self.directory.root = self.directory.insert(self.directory.root, name, phone)

        messagebox.showinfo("Success", f"Inserted/Updated contact: {name}")
        self.clear_entries()
        self.show_all()
        self.draw_tree()

    def search_contact(self):
        name = self.name_entry.get().strip()

        if not name:
            messagebox.showwarning("Input Error", "Please enter a name to search.")
            return

        node = self.directory.search(self.directory.root, name)
        self.output_text.delete(1.0, tk.END)

        if node:
            self.output_text.insert(tk.END, f"Found Contact:\nName: {node.name}\nPhone: {node.phone}\n")
        else:
            self.output_text.insert(tk.END, "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get().strip()

        if not name:
            messagebox.showwarning("Input Error", "Please enter a name to delete.")
            return

        self.directory.root = self.directory.delete(self.directory.root, name)

        messagebox.showinfo("Success", f"Deleted contact (if existed): {name}")
        self.clear_entries()
        self.show_all()
        self.draw_tree()

    def show_all(self):
        self.output_text.delete(1.0, tk.END)
        contacts = self.directory.inorder(self.directory.root)

        if not contacts:
            self.output_text.insert(tk.END, "No contacts found.\n")
        else:
            for name, phone in contacts:
                self.output_text.insert(tk.END, f"Name: {name}, Phone: {phone}\n")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    # ---- Tree Drawing ----
    def draw_tree(self):
        self.canvas.delete("all")
        if not self.directory.root:
            return

        self._draw_node(self.directory.root, 400, 20, 200, 70, 20)

    def _draw_node(self, node, x, y, x_offset, level_gap, radius):
        if node is None:
            return

        if node.left:
            x_left = x - x_offset
            y_left = y + level_gap
            self.canvas.create_line(x, y, x_left, y_left)
            self._draw_node(node.left, x_left, y_left, x_offset // 2, level_gap, radius)

        if node.right:
            x_right = x + x_offset
            y_right = y + level_gap
            self.canvas.create_line(x, y, x_right, y_right)
            self._draw_node(node.right, x_right, y_right, x_offset // 2, level_gap, radius)

        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue")
        self.canvas.create_text(x, y, text=node.name[:10])

    # ---- Benchmark ----
    def benchmark(self):
        self.directory.root = None
        N = 1000

        names = [''.join(random.choices(string.ascii_lowercase, k=7)) for _ in range(N)]
        phones = [''.join(random.choices(string.digits, k=10)) for _ in range(N)]

        start = time.time()
        for i in range(N):
            self.directory.root = self.directory.insert(self.directory.root, names[i], phones[i])
        insert_time = time.time() - start

        start = time.time()
        for name in names:
            self.directory.search(self.directory.root, name)
        search_time = time.time() - start

        start = time.time()
        for name in names[:100]:
            self.directory.root = self.directory.delete(self.directory.root, name)
        delete_time = time.time() - start

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END,
            f"Insertion: {insert_time:.4f}s\nSearch: {search_time:.4f}s\nDelete: {delete_time:.4f}s"
        )

        self.draw_tree()


if __name__ == "__main__":
    root = tk.Tk()
    app = BSTVisualizerApp(root)
    root.mainloop()
