from tkinter import *
from operator import itemgetter
import datetime
import tkinter.messagebox
students = []
def into():
    root = Tk()
    root.title('学生登陆')
    Label1 = Label(root, text='姓名:').grid(row=0, column=0)
    Label2 = Label(root, text='学号:').grid(row=1, column=0)

    v1 = StringVar()
    p1 = StringVar()
    e1 = Entry(root, textvariable=v1)  # Entry 是 Tkinter 用来接收字符串等输入的控件.
    e2 = Entry(root, textvariable=p1)
    e1.grid(row=0, column=1, padx=10, pady=5)  # 设置输入框显示的位置，以及长和宽属性
    e2.grid(row=1, column=1, padx=10, pady=5)
    Button(root, text='登入', width=10, command= lambda: get(e1.get(), e2.get())) \
        .grid(row=2, column=0, sticky=W, padx=10, pady=5)
    mainloop()
def get(e1,e2):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    outTime = "未离开"
    student=[e1,e2,nowTime,outTime]
    students.append(student)
    tkinter.messagebox.showinfo('提示', '登记成功')
def look():
    root = Tk()
    root.title('学生信息')
    text = Text(root, width=120, height=120)
    text.pack(fill=X, side=BOTTOM)
    colume = ["名字：","  学号：","  进入时间：","  离开时间："]
    student = sorted(students, key=itemgetter(1))
    for x in student:
        for i in range (0,4):
            text.insert(END,colume[i])
            text.insert(END,x[i])
        text.insert(END,'\n')# INSERT表示在光标位置插入
    text.see(END)
    text.update()


def get_value():
    return students

