from tkinter import *
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


def show():
    print("学生姓名:%s" % e1.get())  # 获取用户输入的信息
    print("学生学号:%s" % e2.get())


Button(root, text='登入', width=10, command=show) \
    .grid(row=2, column=0, sticky=W, padx=10, pady=5)

Button(root, text='退出', width=10, command=root.quit) \
    .grid(row=2, column=1, sticky=E, padx=10, pady=5)

mainloop()
