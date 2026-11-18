class Teacher:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, teacher):
        self.teacher = teacher

    def show_teacher(self):
        print("Teacher:", self.teacher.name)


teacher1 = Teacher("Maria")
department = Department(teacher1)

department.show_teacher()
