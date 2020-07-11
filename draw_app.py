from tkinter import *
from tkinter.colorchooser import *

WIDTH = 900
HEIGHT = 450

class Application(Frame):

    def __init__(self, master, bgcolor = '#000000'):
        super().__init__(master)
        self.master = master
        self.x = 0
        self.y = 0
        self.bgcolor = bgcolor
        self.fgcolor = '#ff0000'
        self.start_print_flag = False
        self.last_id = 0
        self.pack()
        self.createWIdget()

    def createWIdget(self):
        self.drawrect = Canvas(self, width = WIDTH, height=HEIGHT * 0.9, bg=self.bgcolor)
        self.drawrect.pack()
        btn_start = Button(root, text="开始", name="start")
        btn_start.pack(side="left", padx="10")
        btn_pen = Button(root, text="画笔", name="pen")
        btn_pen.pack(side="left", padx="10")
        btn_rect = Button(root, text="矩形", name="rect")
        btn_rect.pack(side="left", padx="10")
        btn_clear = Button(root, text="清屏", name="clear")
        btn_clear.pack(side="left", padx="10")
        btn_erasor = Button(root, text="橡皮擦", name="erasor")
        btn_erasor.pack(side="left", padx="10")
        btn_line = Button(root, text="直线", name="line")
        btn_line.pack(side="left", padx="10")
        btn_lineArrow = Button(root, text="箭头直线", name="lineArrow")
        btn_lineArrow.pack(side="left", padx="10")
        btn_color = Button(root, text="颜色", name="color")
        btn_color.pack(side="left", padx="10")

        btn_erasor.bind_class('Button', '<1>', self.ButtonEvent)
        self.drawrect.bind('<ButtonRelease-1>', self.draw)

        root.bind('KeyPress-r', self.acc)
        root.bind('KeyPress-y', self.acc)
        root.bind('KeyPress-g', self.acc)

    def ButtonEvent(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name=="line":
            self.drawrect.bind("<B1-Motion>",self.myline)
        elif name=="lineArrow":
            self.drawrect.bind("<B1-Motion>",self.mylineArrow)
        elif name=="rect": self.drawrect.bind("<B1-Motion>",self.myRect)
        elif name=="pen": self.drawrect.bind("<B1-Motion>",self.myPen)
        elif name=="erasor": self.drawrect.bind("<B1-Motion>",self.myErasor)
        elif name=="clear": self.drawrect.delete("all")
        elif name=="color": c = askcolor(color=self.fgcolor,title="选择画笔颜色"); self.fgcolor = c[1]

    def draw(self, event):
        self.start_print_flag = False
        self.last_id = 0    # 在松手时把ID 改变了

    def last_draw(self, event):
        self.drawrect.delete(self.last_id)  # 一直在删除刚刚画上的id
        if not self.start_print_flag:
            self.start_print_flag = True
            self.x = event.x
            self.y = event.y

    def myline(self, event):
        self.last_draw(event)
        self.last_id = self.drawrect.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)


    def mylineArrow(self, event):
        self.last_draw(event)
        self.last_id = self.drawrect.create_line(self.x,self.y,event.x,event.y,arrow=LAST,fill=self.fgcolor)

    def myRect(self, event):
        self.last_draw(event)
        self.last_id = self.drawrect.create_rectangle(self.x,self.y,event.x,event.y,outline=self.fgcolor)


    def myPen(self, event):
        self.last_draw(event)
        self.drawrect.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y


    def myErasor(self, event):
        self.last_draw(event)
        self.drawrect.create_rectangle(event.x-4,event.y-4,event.x+4,event.y+4,fill=self .bgcolor)


    def acc(self, event):
        if event.char == 'r':
            fgcolor = '#ff0000'
        elif event.char == "g":
            self.fgcolor = "#00ff00"
        elif event.char == "y":
            self.fgcolor = "#ffff00"


if __name__ == '__main__':
    root = Tk()
    root.title('future')
    root.geometry(str(WIDTH)+"x"+str(HEIGHT)+"+200+300")
    app = Application(master=root)
    root.mainloop()
