from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.ttk import Scale


class Paint:
    default_pen_size = 1
    default_color = 'black'
    default_canvas_color = "white"

    def __init__(self):
        self.root = Tk()
        self.root.resizable(0, 0)
        self.root.geometry("775x615")
        self.root.title("Paint")
        self.root.iconbitmap('icon.ico')
        self.clear_img = PhotoImage(file="clear.png")
        self.C = Canvas(self.root, bg=self.default_canvas_color,
                        width=600, height=600)
        var = StringVar()
        label = Label(self.root, textvariable=var, relief=GROOVE)
        var.set("Canvas colors")
        label.place(x=640, y=0, height=18)
        var1 = StringVar()
        label1 = Label(self.root, textvariable=var1, relief=GROOVE)
        var1.set("Brushes")
        label1.place(x=655, y=92, height=18)
        var2 = StringVar()
        label2 = Label(self.root, textvariable=var2, relief=GROOVE)
        var2.set("Shapes")
        label2.place(x=658, y=153, height=18)
        var3 = StringVar()
        label3 = Label(self.root, textvariable=var3, relief=GROOVE)
        var3.set("Eraser and clear all")
        label3.place(x=636, y=250, height=18)
        var4 = StringVar()
        label4 = Label(self.root, textvariable=var4, relief=GROOVE)
        var4.set("Color of brushes and shapes")
        label4.place(x=618, y=316, height=18)
        var5 = StringVar()
        label5 = Label(self.root, textvariable=var5, relief=GROOVE)
        var5.set("Width of brushes")
        label5.place(x=635, y=382, height=20)

        self.C.place(x=5, y=5)
        self.clear = Button(self.root, image=self.clear_img,
                            relief=GROOVE, command=lambda:
                            self.C.delete("all")).place(x=684,
                                                        y=276,
                                                        width=36,
                                                        height=36)

        self.pen = PhotoImage(file="pen.png")
        self.pen_button = Button(self.root, image=self.pen,
                                 relief=GROOVE, command=self.set_tool_pen)
        self.pen_button.place(x=625, y=115, width=36, height=36)
        self.line = PhotoImage(file="line.png")
        self.line_button = Button(self.root, image=self.line,
                                  relief=GROOVE, command=self.set_tool_line)
        self.line_button.place(x=624, y=173, width=36, height=36)
        self.high = PhotoImage(file="high.png")
        self.high_button = Button(self.root,
                                  image=self.high, relief=GROOVE,
                                  command=self.set_tool_highlighter)
        self.high_button.place(x=700, y=115, width=36, height=36)
        self.f_pen = PhotoImage(file="marker.png")
        self.arc_button = Button(self.root, image=self.f_pen,
                                 relief=GROOVE, command=self.set_tool_arc)
        self.arc_button.place(x=662, y=115, width=36, height=36)
        self.color_image = PhotoImage(file="color.png")
        self.color_button = Button(self.root, image=self.color_image,
                                   relief=GROOVE, command=self.choose_color)
        self.color_button.place(x=669, y=341, width=36, height=36)
        self.eraser1 = PhotoImage(file="eraser.png")
        self.eraser_button = Button(self.root,
                                    image=self.eraser1, relief=GROOVE,
                                    command=self.set_tool_eraser)
        self.eraser_button.place(x=646, y=276, width=36, height=36)
        self.circle = PhotoImage(file="circle.png")
        self.circle_button = Button(self.root, image=self.circle,
                                    relief=GROOVE,
                                    command=self.set_tool_circle)
        self.circle_button.place(x=660, y=173, width=36, height=36)
        self.rectangle = PhotoImage(file="rect.png")
        self.rect_button = Button(self.root, image=self.rectangle,
                                  relief=GROOVE, command=self.set_tool_rect)
        self.rect_button.place(x=696, y=173, width=39, height=36)
        self.choose_size_button = Scale(self.root, from_=1, to=20,
                                        orient=HORIZONTAL)
        self.rect_change2 = PhotoImage(file='rect2.png')
        self.rect_c1 = Button(self.root,
                              relief=GROOVE,
                              image=self.rect_change2,
                              command=self.set_tool_rect1).place(x=680,
                                                                 y=210,
                                                                 width=39,
                                                                 height=36)
        self.circle_change3 = PhotoImage(file='circle1.png')
        self.circle_c2 = Button(self.root,
                                relief=GROOVE,
                                image=self.circle_change3,
                                command=self.set_tool_circle1).place(
                                                                     x=644,
                                                                     y=210,
                                                                     width=36,
                                                                     height=36)
        self.choose_size_button.place(x=620, y=410, width=130, height=30)

        self.color_frame = LabelFrame(self.root, font=("arial", 10),
                                      relief=RIDGE,
                                      bd=4).place(x=610, y=18,
                                                  width=155, height=66)

        self.canvas_col = Button(self.root, bg="blue", relief=GROOVE,
                                 command=self.c_c).place(x=672,
                                                         y=51, width=30,
                                                         height=30)

        self.canvas_col1 = Button(self.root, bg="green", relief=GROOVE,
                                  command=self.c_c1).place(x=702,
                                                           y=51, width=30,
                                                           height=30)

        self.canvas_col2 = Button(self.root, bg="black", relief=GROOVE,
                                  command=self.c_c2).place(x=612,
                                                           y=21, width=30,
                                                           height=30)
        self.canvas_col3 = Button(self.root, bg="grey", relief=GROOVE,
                                  command=self.c_c9).place(x=642,
                                                           y=21, width=30,
                                                           height=30)

        self.canvas_col3 = Button(self.root, bg="brown", relief=GROOVE,
                                  command=self.c_c4).place(x=672,
                                                           y=21, width=30,
                                                           height=30)

        self.canvas_col3 = Button(self.root, bg="red", relief=GROOVE,
                                  command=self.c_c3).place(x=702,
                                                           y=21, width=30,
                                                           height=30)

        self.canvas_col3 = Button(self.root, bg="orange", relief=GROOVE,
                                  command=self.c_c7).place(x=732,
                                                           y=21, width=30,
                                                           height=30)

        self.canvas_col3 = Button(self.root, bg="yellow", relief=GROOVE,
                                  command=self.c_c6).place(x=732,
                                                           y=51, width=30,
                                                           height=30)

        self.canvas_col3 = Button(self.root, bg="purple", relief=GROOVE,
                                  command=self.c_c8).place(x=642,
                                                           y=51, width=30,
                                                           height=30)

        self.canvas_col3 = Button(self.root, bg="indigo", relief=GROOVE,
                                  command=self.c_c5).place(x=612,
                                                           y=51, width=30,
                                                           height=30)

        self.line_width = self.choose_size_button.get()
        self.color = self.default_color
        self.eraser_color = "white"
        self.paint_color = "black"

        self.line_start_x = None
        self.line_start_y = None

        self.circle_start_x = None
        self.circle_start_y = None

        self.rect_start_x = None
        self.rect_start_y = None

        self.tool_option = 'line'

        self.default()
        self.root.mainloop()

    def c_c(self):
        self.C.configure(background="blue")
        self.eraser_color = "blue"

    def c_c1(self):
        self.C.configure(background="green")
        self.eraser_color = "green"

    def c_c2(self):
        self.C.configure(background="black")
        self.eraser_color = "black"

    def c_c3(self):
        self.C.configure(background="red")
        self.eraser_color = "red"

    def c_c4(self):
        self.C.configure(background="brown")
        self.eraser_color = "brown"

    def c_c5(self):
        self.C.configure(background="indigo")
        self.eraser_color = "indigo"

    def c_c6(self):
        self.C.configure(background="yellow")
        self.eraser_color = "yellow"

    def c_c7(self):
        self.C.configure(background="orange")
        self.eraser_color = "orange"

    def c_c8(self):
        self.C.configure(background="purple")
        self.eraser_color = "purple"

    def c_c9(self):
        self.C.configure(background="grey")
        self.eraser_color = "grey"

    def default(self):
        self.C.bind('<Button-1>', self.draw_start)
        self.C.bind('<B1-Motion>', self.draw_motion)
        self.C.bind('<ButtonRelease-1>', self.draw_end)

    def tool_highlighter(self, event):
        self.line_width = self.choose_size_button.get()
        self.paint_color = self.color
        x1, y1 = event.x - 15, event.y - 1
        x2, y2 = event.x + 15, event.y + 1
        self.C.create_line(x1, y1, x2, y2, fill=self.paint_color,
                           width=self.line_width)

    def choose_color(self):
        self.color = askcolor(color=self.color)[1]

    def tool_pen(self, event):
        self.line_width = self.choose_size_button.get()
        self.paint_color = self.color
        x1, y1 = event.x - 4, event.y - 4
        x2, y2 = event.x + 4, event.y + 4
        self.C.create_oval(x1, y1, x2, y2, fill=self.paint_color,
                           outline=self.paint_color, width=self.line_width)

    def eraser(self, event):
        self.line_width = self.choose_size_button.get()
        x1, y1 = event.x - 4, event.y - 4
        x2, y2 = event.x + 4, event.y + 4
        self.C.create_oval(x1, y1, x2, y2, fill=self.eraser_color,
                           outline=self.eraser_color, width=self.line_width)

    def line_start(self, event):
        self.line_start_x = event.x
        self.line_start_y = event.y

    def line_motion(self, event):
        self.C.delete('temporally_line_coordinates')
        self.C.create_line(self.line_start_x, self.line_start_y,
                           event.x, event.y,
                           fill=self.paint_color, smooth=1,
                           tags='temporally_line_coordinates')

    def line_end(self, event):
        self.line_width = self.choose_size_button.get()
        self.paint_color = self.color
        self.C.create_line(self.line_start_x, self.line_start_y,
                           event.x, event.y, width=self.line_width,
                           fill=self.paint_color, smooth=1)

    def rect_start(self, event):
        self.rect_start_x = event.x
        self.rect_start_y = event.y

    def rect_motion(self, event):
        self.C.delete('temporally_rect_coordinates')
        self.C.create_rectangle(self.rect_start_x, self.rect_start_y,
                                event.x, event.y, outline=self.paint_color,
                                tags='temporally_rect_coordinates')

    def rect_end(self, event):

        self.paint_color = self.color
        self.C.create_rectangle(self.rect_start_x, self.rect_start_y,
                                event.x, event.y, outline=self.paint_color)

    def rect_change(self, event):
        self.paint_color = self.color
        self.C.create_rectangle(self.rect_start_x, self.rect_start_y,
                                event.x, event.y, fill=self.paint_color,
                                outline=self.paint_color)

    def circle_start(self, event):
        self.circle_start_x = event.x
        self.circle_start_y = event.y

    def circle_motion(self, event):
        self.C.delete('temporally_circle_coordinates')
        self.C.create_oval(self.circle_start_x, self.circle_start_y,
                           event.x, event.y, outline=self.paint_color,
                           tags='temporally_circle_coordinates')

    def circle_end(self, event):
        self.paint_color = self.color
        self.C.create_oval(self.circle_start_x, self.circle_start_y,
                           event.x, event.y, outline=self.paint_color)

    def circle_change(self, event):

        self.paint_color = self.color
        self.C.create_oval(self.circle_start_x, self.circle_start_y,
                           event.x, event.y, outline=self.paint_color,
                           fill=self.paint_color)

    def tool_marker(self, event):
        self.paint_color = self.color
        x1, y1 = event.x - 20, event.y - 20
        x2, y2 = event.x + 20, event.y + 20
        self.C.create_oval(x1, y1, x2, y2, fill=self.paint_color)

    def set_tool_pen(self):
        self.tool_option = "pen"
        self.C.bind('<B1-Motion>', self.tool_pen)

    def set_tool_rect1(self):
        self.tool_option = "rect1"
        self.C.bind('<Button-1>', self.draw_start)
        self.C.bind('<B1-Motion>', self.draw_motion)
        self.C.bind('<ButtonRelease-1>', self.draw_end)

    def set_tool_circle1(self):
        self.tool_option = "circle1"
        self.C.bind('<Button-1>', self.draw_start)
        self.C.bind('<B1-Motion>', self.draw_motion)
        self.C.bind('<ButtonRelease-1>', self.draw_end)

    def set_tool_arc(self):
        self.tool_option = "arc"
        self.C.bind('<B1-Motion>', self.tool_marker)

    def set_tool_line(self):
        self.tool_option = 'line'
        self.C.bind('<Button-1>', self.draw_start)
        self.C.bind('<B1-Motion>', self.draw_motion)
        self.C.bind('<ButtonRelease-1>', self.draw_end)

    def set_tool_rect(self):
        self.tool_option = 'rect'
        self.C.bind('<Button-1>', self.draw_start)
        self.C.bind('<B1-Motion>', self.draw_motion)
        self.C.bind('<ButtonRelease-1>', self.draw_end)

    def set_tool_circle(self):
        self.tool_option = 'circle'
        self.C.bind('<Button-1>', self.draw_start)
        self.C.bind('<B1-Motion>', self.draw_motion)
        self.C.bind('<ButtonRelease-1>', self.draw_end)

    def set_tool_highlighter(self):
        self.tool_option = 'high'
        self.C.bind("<B1-Motion>", self.tool_highlighter)

    def set_tool_eraser(self):
        self.tool_option = 'eraser'
        self.C.bind("<B1-Motion>", self.eraser)

    def draw_start(self, event):
        if self.tool_option == 'line':
            self.line_start(event)
        elif self.tool_option == 'circle':
            self.circle_start(event)
        elif self.tool_option == 'pen':
            self.tool_pen(event)
        elif self.tool_option == 'high':
            self.tool_highlighter(event)
        elif self.tool_option == 'arc':
            self.tool_marker(event)
        elif self.tool_option == "eraser":
            self.eraser(event)
        elif self.tool_option == 'rect':
            self.rect_start(event)
        elif self.tool_option == 'rect1':
            self.rect_start(event)
        elif self.tool_option == 'circle1':
            self.circle_start(event)

    def draw_motion(self, event):
        if self.tool_option == 'line':
            self.line_motion(event)
        elif self.tool_option == 'circle':
            self.circle_motion(event)
        elif self.tool_option == 'rect':
            self.rect_motion(event)
        elif self.tool_option == 'rect1':
            self.rect_motion(event)
        elif self.tool_option == 'circle1':
            self.circle_motion(event)

    def draw_end(self, event):
        if self.tool_option == 'line':
            self.line_end(event)
        elif self.tool_option == 'circle':
            self.circle_end(event)
        elif self.tool_option == 'rect':
            self.rect_end(event)
        elif self.tool_option == 'rect1':
            self.rect_change(event)
        elif self.tool_option == 'circle1':
            self.circle_change(event)


Paint()
