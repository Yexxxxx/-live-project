import datetime

nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
students = []
count = 3
for i in range(count):
    name = input('请输入第{i+1}个学生的姓名:')
    number = input('请输入第{i+1}个学生的学号:')
    time = nowTime
    stu_list = [name,number,time]
    students.append(stu_list)

for stu in students:
    for v in stu:
        print(v,end = ' ')
    print()
