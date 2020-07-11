from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
from win32clipboard import *
import win32api
from win32con import *
import wx


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.CreateWidgets()

    def CreateWidgets(self):
        menubar_up = Menu(root)
        menu_file = Menu(menubar_up)
        menu_edit = Menu(menubar_up)
        menubar_up_2 = Menu(root)
        menu_file.add_command(label='新建', command = self.create_new_file)
        menu_file.add_command(label='打开', command = self.open_file)
        menu_file.add_command(label='保存', command = self.save)
        menu_file.add_command(label="退出", accelerator="ctrl+q", command=self.exit)

        menubar_up.add_cascade(label='文件', menu = menu_file)
        menubar_up.add_cascade(label='编辑', menu=menu_edit)
        menu_edit.add_command(label='剪切', command = self.cut)
        menu_edit.add_command(label='粘贴', command = self.paste)
        # menu_file.add_cascade(label='up_2', menu=menubar_up_2)

        root['menu'] = menubar_up

        root.bind("<Control-q>", lambda event: self.exit())

        self.menubar = Menu(root)
        self.menubar.add_command(label='设置颜色', command=self.color_set)
        menubar2 = Menu(root)
        menubar2.add_command(label='剪切', command=self.cut)
        menubar2.add_command(label='粘贴', command=self.paste)
        menubar2.add_command(label='保存', command=self.save)



        self.menubar.add_cascade(label='编辑', menu=menubar2)
        self.text = Text(self, width = 30, height = 50)
        self.text.pack()
        self.text.bind('<Button-3>', self.create_window)

    def create_new_file(self):
        self.text.delete('1.0', 'end')
        self.file = asksaveasfilename(title='另存为', initialfile='未命名', filetypes=[('文本文档','*.txt')], defaultextension='*.txt')
        self.save()

    def open_file(self):
        try:
            with askopenfile(title='打开文件' ) as f:
                self.text.delete('1.0', 'end')
                self.text.insert(INSERT, f.read())
                self.file = f.name
        except:
            print('open error')

    def exit(self):
        root.quit()

    def create_window(self, event):
        self.menubar.post(event.x_root, event.y_root)

    def color_set(self):
        color1 = askcolor(color='white', title='color')
        root.config(bg=color1[1])

    def cut(self):
        """剪切程序!"""
        """OpenClipboard()
        EmptyClipboard()
        SetClipboardData()
        CloseClipboard()"""
        win32api.keybd_event(17,0,0,0)
        win32api.keybd_event(88,0,0,0)
        win32api.keybd_event(88, 0, KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(17, 0, KEYEVENTF_KEYUP, 0)



    def paste(self):
        OpenClipboard()
        content = GetClipboardData(CF_TEXT)
        CloseClipboard()
        self.text.insert(INSERT, content)


    def save(self):
        try:
            with open(self.file, 'w') as f:
                content = self.text.get(1.0, END)
                f.write(content)
        except:
            print('error')

if __name__ == '__main__':
    root = Tk()
    app = Application(master = root)
    root.title = 'future'
    root.geometry('300x400+200+400')
    root.mainloop()