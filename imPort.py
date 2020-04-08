import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
students = []
def shuru():
        count = 3
        for i in range(count):
                name = input('请输入第{i+1}个学生的姓名:')
                number = input('请输入第{i+1}个学生的学号:')
                time = nowTime
                stu_list = [name,number,time]
                students.append(stu_list)
def find():
        xuehao=input("")
        for i in range(len(students)):
                mid=students[i]
                mid_no=mid[1]
                if(xuehao==mid_no):
                        print(mid)
                        break
def sort():
    from operator import itemgetter
    student=sorted(students,key=itemgetter(1))
    print(student)
