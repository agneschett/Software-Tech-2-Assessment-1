import tkinter as tk
from tkinter import messagebox

NODE_WIDTH = 80
NODE_HEIGHT = 40
VERTICAL_GAP = 10
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 500

class StackVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Visualizer")

        self.stack = []

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack(pady=20)

        control_frame = tk.Frame(root)
        control_frame.pack()

        tk.Label(control_frame, text="Push Value:").grid(row=0, column=0)
        self.push_entry = tk.Entry(control_frame, width=10)
        self.push_entry.grid(row=0, column=1)

        push_btn = tk.Button(control_frame, text="Push", command=self.push_value)
        push_btn.grid(row=0, column=2, padx=5)

        pop_btn = tk.Button(control_frame, text="Pop", command=self.pop_value)
        pop_btn.grid(row=1, column=2, pady=5)

        self.status_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.draw_stack()

    def draw_node(self, x, y, data):
        rect = self.canvas.create_rectangle(x, y, x + NODE_WIDTH, y + NODE_HEIGHT, fill="lightblue", outline="black", width=2)
        self.canvas.create_text(x + NODE_WIDTH/2, y + NODE_HEIGHT/2, text=str(data), font=("Arial", 16))
        return rect

    def draw_stack(self):
        self.canvas.delete("all")
        x = (CANVAS_WIDTH - NODE_WIDTH) // 2
        y = CANVAS_HEIGHT - NODE_HEIGHT - 10
        for val in reversed(self.stack):
            self.draw_node(x, y, val)
            y -= NODE_HEIGHT + VERTICAL_GAP
        # Draw label for top
        if self.stack:
            self.canvas.create_text(x + NODE_WIDTH + 40, CANVAS_HEIGHT - NODE_HEIGHT - 10, text="Top", font=("Arial", 12), fill="red")

    def push_value(self):
        try:
            val = int(self.push_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter an integer value to push.")
            return
        self.stack.append(val)
        self.push_entry.delete(0, tk.END)
        self.status_label.config(text=f"Pushed {val} onto stack")
        self.draw_stack()

    def pop_value(self):
        if len(self.stack) == 0:
            messagebox.showinfo("Empty Stack", "Stack is empty. Cannot pop.")
            return
        val = self.stack.pop()
        self.status_label.config(text=f"Popped {val} from stack")
        self.draw_stack()

if __name__ == "__main__":
    root = tk.Tk()
    app = StackVisualizer(root)

    # Example test cases:
    # app.stack = [10, 20, 30]
    # app.draw_stack()
    root.mainloop()
