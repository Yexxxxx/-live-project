import time
import datetime
# 做桌面编程的
import tkinter as tk

class APP:
    # 魔术方法
    # 初始化用的
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = '团队Github实战训练'
        # 软件名
        self.root = tk.Tk(className=self.title)

        # 姓名 StringVar() 定义字符串变量
        self.into = tk.StringVar()
        self.leve = tk.StringVar()
        self.xid = tk.IntVar()
        self.yid = tk.IntVar()
        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        # 控件内容设置
        group = tk.Label(frame_1, text='在校记录登记：', padx=10, pady=10)

        lablex = tk.Label(frame_2, text='登记进入校姓名：')
        labley= tk.Label(frame_2, text='登记离开校园姓名：')
        lable_xid = tk.Label(frame_2, text='学号：')
        lable_yid = tk.Label(frame_2, text='学号：')
        # 输入框声明
        entry_x = tk.Entry(frame_2, textvariable=self.into, highlightcolor='Fuchsia', highlightthickness=1, width=15)
        entry_y = tk.Entry(frame_2, textvariable=self.leve, highlightcolor='Fuchsia', highlightthickness=1, width=15)
        entry_xid = tk.Entry(frame_2, textvariable=self.xid, highlightcolor='Fuchsia', highlightthickness=1, width=15)
        entry_yid = tk.Entry(frame_2, textvariable=self.yid, highlightcolor='Fuchsia', highlightthickness=1, width=15)
        #time= tk.datetime.now() + '\n'
        # 控件布局 显示控件在你的软件上
        frame_1.pack()
        frame_2.pack()
        # 确定控件的位置 wow 行 column 列
        group.grid(row=0, column=0)
        lablex.grid(row=0, column=0)
        lable_xid.grid(row=0, column=2)
        labley.grid(row=1, column=0)
        lable_yid.grid(row=1, column=2)
        entry_x.grid(row=0, column=1)
        entry_xid.grid(row=0, column=3)
        entry_y.grid(row=1, column=1)
        entry_yid.grid(row=1, column=3)
        #time.grid(row=1, column=4)
        # 启动GUI程序的函数
    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == "__main__":
    app = APP()
    app.loop()
