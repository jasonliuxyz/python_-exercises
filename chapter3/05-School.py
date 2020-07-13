#创建北京和成都两个校区
#创建Linux/python两个课程
#创建北京校区的Python 3期课程和成都校区的Linux 1期课程
#管理员创建了北京校区的学员小张，并将其分配在了Python3期
#管理员创建了讲师小周，并将其分配给了Python3期
#讲师小周创建了一条Python3期的上课记录 Day02
#讲师小周为Day02这节课所有的学员批改了作业，小张得了A，小王得了B
#学员小张查看了自己所报的课程
#学员小张查看了自己在Python3的成绩列表然后退出了
#学员小张给了讲师小周好评

Course_list = []
class School(object):
    def __init__(self, school_name):
        self.school_name = school_name
        self.student_list = []
        self.teacher_list = []
        
        global Course_list
        
    def hire(self, obj):
        self.teacher_list.append(obj.name)
        print("我们现在有一个老师{}".format(obj.name))
        
    def enroll(self, obj):
        self.student_list.append(obj.name)
        print("我们现在有一个新学员{}".format(obj.name))
        
class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)
        
        print("我们现在有了{}的{}的{}".format(self.school_name, self.code, self.course))
        
    def course_info(self):
        print("课程大纲{} 是day01, day02, day03".format(self.course))
        
Python = Grade("BJ", 3, "python")
Linux = Grade("CD", 1, "Linux")

class School_member(object):
    def __init__(self, name, age, sex, role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []
        
        print("我叫{}, 我是一个{}".format(self.name, self.role)) 

stu_num_id = 00
class Student(School_member):
    def __init__(self, name, age, sex, role, course):
        super(Student,self).__init__(name, age, sex, role)
        global stu_num_id
        stu_num_id += 1
        stu_id = course.school_name + "S" + str(course.code) + str(stu_num_id).zfill(2)
        
        self.id = stu_id
        self.mark_list = {}
        
    def study(self, course):
        print("我来这里学习{}课，我的学号是{}".format(course.course, self.id))
        
    def pay(self, course):
        print("我交了1000块钱给{}".format(course.course))
        self.course_list.append(course.course)
        
    def Praise(self, obj):
        print("{}觉得{}课真棒".format(obj.name, obj.name))
        
    def mark_check(self):
        for i in self.mark_list.items():
            print(i)
    
    def out(self):
        print('我离开了')
        
tea_num_id=00
class Teacher(School_member):
    def __init__(self, name, age, sex, role, course):       
        super(Teacher,self).__init__(name, age, sex, role)
        global tea_num_id
        tea_num_id +=1
        tea_id = course.school_name + "T" + str(course.code) + str(tea_num_id).zfill(2)
        self.id = tea_id
        
    def teach(self, course):
        print("我来这里讲{}课，我的id是{}".format(course.course, self.id))
        
    def record_mark(self, Date, course, obj, level):
        obj.mark_list["Day"+Date] = level
        
a = Student('小张', 18, 'M', 'student', Python)
Python.enroll(a)
a.study(Python)
a.pay(Python)

b = Student('小王', 22, 'F', 'student', Python)
Python.enroll(b)
b.study(Python)
b.pay(Python)

#c = Teacher('小周', 30, 'M', 'teacher', Python)
c = Teacher('小周', 30, 'M', 'teacher', Python)
Python.hire(c)
c.teach(Python)
c.record_mark('1', Python, a, 'A')
c.record_mark('1', Python, b, 'B')
c.record_mark('2', Python, a, 'A')
c.record_mark('2', Python, b, 'B')

print(b.course_list)
b.mark_check()
b.out()
