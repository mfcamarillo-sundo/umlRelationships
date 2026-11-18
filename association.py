class Subject:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name

    def study(self, subject):
        print(self.name, "is studying", subject.name)


student = Student("Alex")
subject = Subject("Biology")

student.study(subject)
