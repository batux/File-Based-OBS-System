from MenuDisplayer import MenuDisplayer
from ChoiceSelector import ChoiceSelector
from StudentRecorder import StudentRecorder
from LessonRecorder import LessonRecorder
from StudentFileOperation import StudentFileOperation
from LessonFileOperation import LessonFileOperation
from Lesson import Lesson

class OBSSytem:

    def __init__(self):
        self.studentFileOperation = StudentFileOperation()
        self.lessonFileOperation = LessonFileOperation()

    def start(self):

        while True:

            MenuDisplayer.show()
            choice =  ChoiceSelector.selectOperation()

            if choice == 8:
                break
                
            if choice == 1:
                student = StudentRecorder.create()
                self.studentFileOperation.write(student)
            elif choice == 2:
                lesson = LessonRecorder.create()
                self.lessonFileOperation.write(lesson)
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                no = StudentRecorder.find()
                self.studentFileOperation.find(no)
            elif choice == 6:
                no = StudentRecorder.find()
                self.studentFileOperation.update(no)
            elif choice == 7:
                code = LessonRecorder.find()
                self.lessonFileOperation.update(code)