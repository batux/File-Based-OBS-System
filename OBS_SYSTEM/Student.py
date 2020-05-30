
class Student:

    def __init__(self, no, name, surname, department, age):
        self.no = no
        self.name = name
        self.surname = surname
        self.department = department
        self.age = age
    
    def prepareSummaryAsWritableFormat(self):

        content = ""
        content += str(self.no) + "\n"
        content += self.name + "\n"
        content += self.surname + "\n"
        content += self.department + "\n"
        content += str(self.age) + "\n"
        return content

    def toString(self):

        content = ""
        content += str(self.no)
        content += self.name
        content += self.surname
        content += self.department
        content += str(self.age)
        return content