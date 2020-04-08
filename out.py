from tkinter import *
from operator import itemgetter
import stureg
import datetime
import tkinter.messagebox
students = stureg.get_value()
print(students)
def find():
    root = Tk()
    root.title('学生登陆')
    Label2 = Label(root, text='学号:').grid(row=1, column=0)
    p1 = StringVar()
    e2 = Entry(root, textvariable=p1)
    e2.grid(row=1, column=1, padx=10, pady=5)# 设置输入框显示的位置，以及长和宽属性
    Button(root, text='登入', width=10, command= lambda:result(e2.get())) \
        .grid(row=2, column=0, sticky=W, padx=10, pady=5)
    mainloop()

def result(e2):
    num = e2
    for i in range(len(students)):
        mid = students[i]
        mid_no = mid[1]
        if (num == mid_no):
            if (mid[3] != "未离开"):
                tkinter.messagebox.showinfo('提示', '请先入校登记')
                break
            outTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            mid[3] = outTime
            tkinter.messagebox.showinfo('提示', '离校成功，数据更新')
            break
        else:
            tkinter.messagebox.showinfo('提示','查无此人')