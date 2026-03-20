from tkinter import *
import math

class KochSnowflake:
    def __init__(self):
        window = Tk()
        window.title("Koch Snowflake")

        self.width = 400
        self.height = 400
        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Label(frame1, text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()
        Entry(frame1, textvariable=self.order, justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display Koch Snowflake", command=self.display).pack(side=LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")

        try:
            order = int(self.order.get())
        except ValueError:
            return

        size = 300
        h = size * math.sqrt(3) / 2

        p1 = [self.width/2 - size/2, self.height/2 + h/3]
        p2 = [self.width/2 + size/2, self.height/2 + h/3]
        p3 = [self.width/2, self.height/2 - 2*h/3]

        self.drawKoch(order, p1, p2)
        self.drawKoch(order, p2, p3)
        self.drawKoch(order, p3, p1)

    def drawKoch(self, order, p1, p2):
        if order == 0:
            self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="line")
            return

        dx = (p2[0] - p1[0]) / 3
        dy = (p2[1] - p1[1]) / 3

        pA = [p1[0] + dx, p1[1] + dy]
        pB = [p1[0] + 2*dx, p1[1] + 2*dy]

        s = math.sqrt(dx**2 + dy**2)

        mx = (pA[0] + pB[0]) / 2
        my = (pA[1] + pB[1]) / 2

        nx = -dy / s
        ny =  dx / s

        h = s * math.sqrt(3) / 2

        pC = [mx + nx * h, my + ny * h]

        cx, cy = self.width / 2, self.height / 2
        d_mid2 = (mx - cx)**2 + (my - cy)**2
        d_peak2 = (pC[0] - cx)**2 + (pC[1] - cy)**2

        if d_peak2 < d_mid2:
            pC = [mx - nx * h, my - ny * h]

        self.drawKoch(order - 1, p1, pA)
        self.drawKoch(order - 1, pA, pC)
        self.drawKoch(order - 1, pC, pB)
        self.drawKoch(order - 1, pB, p2)

KochSnowflake()