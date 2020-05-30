from FileWriter import FileWriter
from FileReader import FileReader
from Student import Student
from StudentRecorder import StudentRecorder
from SeekOffsetCalculator import SeekOffsetCalculator
from os import path

class StudentFileOperation(FileReader, FileWriter, SeekOffsetCalculator):

    filePath = "/tmp/students.txt"
    studentFileIndex = {}

    def __init__(self):
        if path.isfile(self.filePath):
            with FileReader.open(self.filePath) as file:
                SeekOffsetCalculator.createRecordFileIndex(self.studentFileIndex, file, 4)


    def write(self, student):
        
        if student is None:
            return
        
        try:
            with FileWriter.open(self.filePath) as file:
                studentSummary = student.prepareSummaryAsWritableFormat()
                file.write(studentSummary)
                newStudentOffSetValue = len(studentSummary)
                self.studentFileIndex[student.no] = newStudentOffSetValue
                print("Öğrenci başarıyla kaydedildi.")
        except Exception as e:
            print(f"Hata: {e}")


    def find(self, no):

        if no < 0:
            print("Record is not a student!")
            return
        
        seekSummary = SeekOffsetCalculator.determineSeekValueAndOffset(self.studentFileIndex, no)
        jumpToSeekValue = seekSummary["jumpToSeekValue"]
        currentStudentOffset = seekSummary["currentRecordOffset"]

        with FileReader.open(self.filePath) as file:
            file.seek(jumpToSeekValue)
            currentStudentLines = file.read(currentStudentOffset)
            print("*** Öğrenci Kaydı ***")
            print(currentStudentLines)
            

    def update(self, no):

        if no < 0:
            print("Record is not a student!")
            return

        seekSummary = SeekOffsetCalculator.determineSeekValueAndOffset(self.studentFileIndex, no)
        jumpToSeekValue = seekSummary["jumpToSeekValue"]
        currentStudentOffset = seekSummary["currentRecordOffset"]

        firstPartLines = []
        lastPartLines = []
        with FileReader.open(self.filePath) as file:
            file.seek(0)
            firstPartLines = file.read(jumpToSeekValue).splitlines()
            print(firstPartLines)
            file.seek(currentStudentOffset + jumpToSeekValue)
            lastPartLines = file.read().splitlines()
            print(lastPartLines)


        with FileWriter.reset(self.filePath) as file:
            file.seek(0)
            if len(firstPartLines) > 0:
                content = ""
                for line in firstPartLines:
                    content += line + "\n"
                file.writelines(content)


        with FileWriter.update(self.filePath) as file:
            file.seek(jumpToSeekValue)
            student = StudentRecorder.create()
            studentSummary = student.prepareSummaryAsWritableFormat()
            file.write(studentSummary)
            newStudentOffSetValue = len(studentSummary)
            self.studentFileIndex[student.no] = newStudentOffSetValue
            print("Öğrenci başarıyla güncellendi.")
        
        with FileWriter.open(self.filePath) as file:
            content = ""
            for line in lastPartLines:
                content += line + "\n"
            file.writelines(content)