from tkinter import *
from tkinter import messagebox


class Counter(Frame):

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.pack()
        self.create_items()

    def create_items(self):
        btnText = (("MC","M+","M-","MR"), ("(","/","* ", ")"), (7,8,9,"-"), (4,5,6,"+"), (1,2,3,"="), (0,".", "C"))
        self.vi = StringVar()
        self.vi.set('')
        self.entry1 = Entry(self, textvariable=self.vi)
        self.entry1.grid(row=0, column=0, columnspan=4, ipady=20)
        for iindex, i in enumerate(btnText):
            for jindex, j in enumerate(i):
                if j == '=':

                        Button(self, text=j, command= self.eval_value).grid(column=jindex, row=iindex+1, rowspan=2, sticky=NSEW)


                elif j == 'C':
                    Button(self, text=j, command=self.be_zero).grid(column=jindex, row=iindex+1, sticky=NSEW)
                elif iindex == 0:
                    Button(self, text=j).grid(column=jindex, row=iindex + 1, sticky=NSEW)
                else:
                    self.butj = Button(self, text=j, command=lambda text = j : self.vi.set(self.vi.get() + str(text)))  # 神奇！
                    self.butj.grid(row=iindex+1,column=jindex,sticky=NSEW)

    def eval_value(self):
        #  lambda text=j: self.vi.set(eval(self.vi.get()))
        try:
            self.vi.set(eval(self.vi.get()))
        except:
           messagebox.showinfo('error!', 'please restart')

    def be_zero(self):
        new_vi=''
        self.vi.set(new_vi)
        self.entry1.delete('1.0', 'END')


if __name__ == '__main__':
    root = Tk()
    root.title = '计算器--future'
    root.geometry('500x500+500+500')
    app = Counter(root)
    mainloop()



