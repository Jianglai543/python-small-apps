from tkinter import *
import cards_tools


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.get_it = False
        if self.master == root:
            self.create_items()


    def create_items(self):
        but1 = Button(master=self, text='confirm', command=self.confirm)
        but1.pack()
        # self.but2 = Button(master=self, text='应用', command=self.utilize)
        self.text1 = Text(self)
        self.text1.pack()

        self.string_who = StringVar()

        self.labelwho = Label(self, text='你要查什么：（手机和名字）')
        self.labelwho.pack()
        self.entrywho = Entry(self, textvariable=self.string_who)
        self.entrywho.pack()

        self.v1 = StringVar()
        self.v1.set('1')

        self.r1 = Radiobutton(root, text="添加", value="1", variable=self.v1)
        self.r2 = Radiobutton(root, text="显示全部", value="2", variable=self.v1)
        self.r3 = Radiobutton(root, text="查找", value="3", variable=self.v1)
        self.r4 = Radiobutton(root, text="保存", value="4", variable=self.v1)
        self.r5 = Radiobutton(root, text="菜单", value="5", variable=self.v1)

        self.r1.pack(side="left")
        self.r2.pack(side="left")
        self.r3.pack(side="left")
        self.r4.pack(side="left")
        self.r5.pack(side="left")


    def confirm(self):
        if self.v1.get() == '1':
            self.text1.insert(1.0, '你选择了添加\n')
            if not self.get_it:self.createWidgets2()

        if self.v1.get() == '2':

            self.text1.insert(1.0, '你选择了显示全部\n')
            self.content = list(cards_tools.show_all())
            self.text1.insert(1.0, '\n')
            self.text1.insert(1.0, self.content)

        if self.v1.get() == '3':
            self.text1.insert(1.0, '你选择了查找\n')
            self.search = list(cards_tools.check_menu(self.string_who.get()))
            self.text1.insert(1.0, '\n')
            self.text1.insert(1.0, self.search)
        if self.v1.get() == '4':
            self.text1.insert(1.0, '你选择了保存\n')
            cards_tools.save_menu()
        if self.v1.get() == '5':
            self.text1.insert(1.0, '你选择了显示菜单\n')
            self.text1.insert(1.0, "4. 保存数据库信息\n")
            self.text1.insert(1.0, "3. 查询数据库信息\n")
            self.text1.insert(1.0, "2. 显示全部数据库信息\n")
            self.text1.insert(1.0, "1. 添加数据库信息\n")
            self.text1.insert(1.0, "\n")
            self.text1.insert(1.0, "*" * 50)
            self.text1.insert(1.0, '数据库信息管理 1.0\n')


    def createWidgets2(self):
        self.get_it = True
        self.label1 = Label(self, text='姓名')
        self.label1.pack()
        self.string1 = StringVar()
        self.entry = Entry(self, textvariable=self.string1)
        self.entry.pack()

        self.label2 = Label(self, text='电话')
        self.label2.pack()
        self.string2 = StringVar()
        self.entry2 = Entry(self, textvariable=self.string2)
        self.entry2.pack()

        self.label3 = Label(self, text='邮箱')
        self.label3.pack()
        self.string3 = StringVar()
        self.entry3 = Entry(self, textvariable=self.string3)
        self.entry3.pack()

        self.label4 = Label(self, text='QQ')
        self.label4.pack()
        self.string4 = StringVar()
        self.entry4 = Entry(self, textvariable=self.string4)
        self.entry4.pack()

        self.btn01 = Button(self, text="login", command=self.login)
        self.btn01.pack()
    def login(self):
        cards_tools.add_menu(self.string1.get(), self.string2.get(),self.string3.get(), self.string4.get())


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x900+0+0')
    root.title('The Future')

    """root2 = Toplevel()
    root2.geometry('400x400+300+300')
    root2.title('The Future')
    root2.bind('<Button>')
    root2.mainloop()"""

    app = Application(master=root)
    root.mainloop()
