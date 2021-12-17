from tkinter import *
from tkinter import Label

state = "nothing"
screen_side = 650
x_marge = 100
y_marge = 55
num_square_side = 50
square_side = (screen_side - 2 * x_marge) / num_square_side
pencil_size = 0
grid_color_array = []


def Main():
    def restart(event):
        global state
        if event.char == "r":
            fillW()
            state = "nothing"

    def focusRoot(event=None):
        root.focus_set()

    # Create Main Window -- root
    root = Tk()
    root.title("Pixel Art")
    root.resizable(False, False)
    root.geometry("650x650")
    root["bg"] = "#999AED"
    root.bind("<Key>", restart)

    def cursorGridPos(x, y):
        for i in range(1, num_square_side + 1):
            for j in range(1, num_square_side + 1):
                if isBetween(x, x_marge + square_side * (i - 1), x_marge + square_side * i) and \
                        isBetween(y, y_marge + square_side * (j - 1), y_marge + square_side * j):
                    return [i, j]

    def isBetween(a, b, c):
        if (b <= a <= c) or (c <= a <= b):
            return True
        else:
            return False

    def returnEdges(edges, pos_to_color):
        steps = [
            [0, 1],
            [1, 0],
            [-1, 0],
            [0, -1]
        ]
        edges_to_return = []
        for edge in edges:
            for step in steps:
                new_x = edge[0] + step[0]
                new_y = edge[1] + step[1]
                if [new_x, new_y] not in edges_to_return and [new_x, new_y] not in pos_to_color:
                    edges_to_return.append([new_x, new_y])
        return edges_to_return

    def clickedOnGrid(event):
        global grid_color_array
        focusRoot()
        if isBetween(event.x, x_marge, x_marge + num_square_side * square_side) \
                and isBetween(event.y, y_marge, y_marge + num_square_side * square_side):
            pos = cursorGridPos(event.x, event.y)
            if not state == "nothing":
                pos_to_color = [pos]
                # for i in range(pencil_size):
                #
                edges = [pos]
                for i in range(pencil_size):
                    new_edges = returnEdges(edges, pos_to_color)
                    for edge in new_edges:
                        pos_to_color.append(edge)
                    edges = new_edges
                for pos in pos_to_color:
                    if isBetween(pos[0], 1, num_square_side) and isBetween(pos[1], 1, num_square_side):
                        if state == "#999AED":
                            outline = "black"
                        else:
                            outline = ""
                        w.create_rectangle(x_marge + (pos[0] - 1) * square_side,
                                           y_marge + (pos[1] - 1) * square_side,
                                           x_marge + pos[0] * square_side,
                                           y_marge + pos[1] * square_side,
                                           fill=state, outline=outline)

    def changeColor(color):
        global state
        state = color
        focusRoot()

    # Create the board
    w = Canvas(root, width=screen_side, height=screen_side)

    def updateSquareSize():
        global num_square_side
        global square_side
        focusRoot()
        if not square_size_input.get() == "" and square_size_input.get().isnumeric():
            num_square_side = int(square_size_input.get())
            square_side = (screen_side - 2 * x_marge) / num_square_side
            fillW()

    def updatePencilSize():
        global pencil_size
        if not pencil_size_input.get() == "" and pencil_size_input.get().isnumeric():
            pencil_size = int(pencil_size_input.get())

    def fillW():
        w.create_rectangle(0, 0, 650, 650, fill="#999AED", outline="#999AED")
        for i in range(num_square_side + 1):
            w.create_line(i * square_side + x_marge, y_marge, i * square_side + x_marge,
                          y_marge + num_square_side * square_side)
            w.create_line(x_marge, i * square_side + y_marge, x_marge + num_square_side * square_side,
                          i * square_side + y_marge)
        w.bind("<B1-Motion>", clickedOnGrid)
        w.bind("<Button-1>", clickedOnGrid)
        w.pack()

    fillW()

    square_size_message = Label(root, text="Set size", bg="#999AED")
    square_size_message.place(relx=0.07, rely=0.27, anchor=CENTER)
    square_size_input = Entry(root, width=4, bg="#999AED")
    square_size_input.place(relx=0.07, rely=0.30, anchor=CENTER)
    square_size_button = Button(root, text="update size", width=7, height=1, bg="#999AED", command=updateSquareSize)
    square_size_button.place(relx=0.07, rely=0.34, anchor=CENTER)
    pencil_size_message = Label(root, text="Set pencil", bg="#999AED")
    pencil_size_message.place(relx=0.07, rely=0.44, anchor=CENTER)
    pencil_size_input = Entry(root, width=4, bg="#999AED")
    pencil_size_input.place(relx=0.07, rely=0.47, anchor=CENTER)
    pencil_size_button = Button(root, text="update size", width=7, height=1, bg="#999AED", command=updatePencilSize)
    pencil_size_button.place(relx=0.07, rely=0.51, anchor=CENTER)

    # Create title and buttons
    headline = Label(root, text="Pixel Art", bg="#999AED", font=('Helvetica bold', 25))
    green_button = Button(root, text="green", bg="green", fg="white", width=12, command=lambda: changeColor("green"))
    cyan_button = Button(root, text="cyan", bg="cyan", fg="black", width=12, command=lambda: changeColor("cyan"))
    blue_button = Button(root, text="blue", bg="blue", fg="white", width=12, command=lambda: changeColor("blue"))
    violet_button = \
        Button(root, text="purple", bg="purple", fg="white", width=12, command=lambda: changeColor("purple"))
    red_button = Button(root, text="red", bg="red", fg="white", width=12, command=lambda: changeColor("red"))
    orange_button = \
        Button(root, text="orange", bg="orange", fg="white", width=12, command=lambda: changeColor("orange"))
    pink_button = Button(root, text="pink", bg="pink", fg="black", width=12, command=lambda: changeColor("pink"))
    yellow_button = \
        Button(root, text="yellow", bg="yellow", fg="black", width=12, command=lambda: changeColor("yellow"))
    grey_button = Button(root, text="grey", bg="grey", fg="white", width=12, command=lambda: changeColor("grey"))
    white_button = Button(root, text="white", bg="white", fg="black", width=12, command=lambda: changeColor("white"))
    black_button = Button(root, text="black", bg="black", fg="white", width=12, command=lambda: changeColor("black"))
    eraser_button = \
        Button(root, text="eraser", bg="white", fg="black", width=12, command=lambda: changeColor("#999AED"))

    # Place title and buttons
    headline.place(relx=0.5, rely=0.04, anchor=CENTER)
    green_button.place(relx=0.12, rely=0.88, anchor=CENTER)
    cyan_button.place(relx=0.37, rely=0.88, anchor=CENTER)
    blue_button.place(relx=0.62, rely=0.88, anchor=CENTER)
    violet_button.place(relx=0.88, rely=0.88, anchor=CENTER)
    red_button.place(relx=0.37, rely=0.94, anchor=CENTER)
    orange_button.place(relx=0.62, rely=0.94, anchor=CENTER)
    pink_button.place(relx=0.12, rely=0.94, anchor=CENTER)
    yellow_button.place(relx=0.88, rely=0.94, anchor=CENTER)
    grey_button.place(relx=0.37, rely=0.82, anchor=CENTER)
    white_button.place(relx=0.12, rely=0.82, anchor=CENTER)
    black_button.place(relx=0.62, rely=0.82, anchor=CENTER)
    eraser_button.place(relx=0.88, rely=0.82, anchor=CENTER)

    root.mainloop()


if __name__ == '__main__':
    Main()
