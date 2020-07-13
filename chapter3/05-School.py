
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
