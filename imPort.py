import datetime
from operator import itemgetter
import stureg
students = []
def add(e1,e2):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = e1
    number = e2
    time = nowTime
    stu_list = [name,number,time]
    students.append(stu_list)
    print(students)

def sort():
    student=sorted(students,key=itemgetter(1))
    print(student)