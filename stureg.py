from tkinter import *
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
    Button(root, text='登入', width=10, command= lambda: show(e1.get(), e2.get())) \
        .grid(row=2, column=0, sticky=W, padx=10, pady=5)
    mainloop()
def show(e1,e2):
    student=[e1,e2]
    students.extend(student)
    print("学生姓名:%s" % e1)  # 获取用户输入的信息
    print("学生学号:%s" % e2)
    print(students)


