from tkinter import *
import sys
sys.path.append('E:\Github\-live-project')
import stureg
def newwind():
    winNew = Toplevel(root)
    winNew.geometry('360x360')
    winNew.title('新窗体')
    lb2 = Label(winNew, text='我在新窗体上')
    lb2.place(relx=0.2, rely=0.2)
    btClose = Button(winNew, text='关闭', command=winNew.destroy)
    btClose.place(relx=0.7, rely=0.5)
root = Tk()
root.title('学生进出登记界面')
root.geometry('360x360')
lb1 = Label(root,text='学生进出登记', font=('宋体',16, 'bold'))
lb1.place(relx=0.2, rely=0.2)
Button(root, text='登记', width=10, command = stureg.into) \
    .grid(row=2, column=0, sticky=W, padx=10, pady=5)
Button(root, text='查询', width=10) \
    .grid(row=2, column=1, sticky=E, padx=10, pady=5)
mainmenu = Menu(root)
menuFile = Menu(mainmenu)
mainmenu.add_cascade(label='菜单', menu=menuFile)
menuFile.add_command(label='新窗体', command=newwind)
menuFile.add_separator()
menuFile.add_command(label='退出', command=root.destroy)
root.config(menu=mainmenu)
root.mainloop()