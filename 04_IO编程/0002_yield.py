from collections import deque
import time


def student(name, homeworks):
    for homework in homeworks.items():
        yield (name, homework[0], homework[1])  # 学生"生成"作业给老师


class Teacher(object):
    def __init__(self, students):
        self.students = deque(students)

    def handle(self):
        index_00 = len(self.students)
        print(index_00)
        """老师处理学生作业"""
        while index_00:
            student = self.students.pop()
            try:
                homework = next(student)
                print('handling', homework[0], homework[1], homework[2])
            except StopIteration:
                pass
            else:
                self.students.appendleft(student)

            index_00 = len(self.students)
            print(index_00)
            time.sleep(1)


genor_00 = [
    student('Student1', {'math': '1+1=2', 'cs': 'operating system'}),
    student('Student2', {'math': '2+2=4', 'cs': 'computer graphics'}),
    student('Student3', {'math': '3+3=5', 'cs': 'compiler construction'})
]

# print(type(genor_00))
index_00 = student('Student1', {'math': '1+1=2', 'cs': 'operating system'})
index_01 = next(index_00)
print(index_01[0])
print(index_01[1])
print(index_01[2])
Teacher(genor_00).handle()
