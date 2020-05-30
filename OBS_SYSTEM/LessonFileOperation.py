from FileReader import FileReader
from FileWriter import FileWriter
from SeekOffsetCalculator import SeekOffsetCalculator
from LessonRecorder import LessonRecorder
from os import path

class LessonFileOperation(FileReader, FileWriter, SeekOffsetCalculator):

    filePath = "/tmp/lessons.txt"
    lessonFileIndex = {}

    def __init__(self):
        if path.isfile(self.filePath):
            with FileReader.open(self.filePath) as file:
                SeekOffsetCalculator.createRecordFileIndex(self.lessonFileIndex, file, 2)

    def write(self, lesson):
        
        try:
            with FileWriter.open(self.filePath) as file:
                lessonSummary = lesson.prepareSummaryAsWritableFormat()
                file.write(lessonSummary)
                newLessonOffSetValue = len(lessonSummary)
                self.lessonFileIndex[lesson.code] = newLessonOffSetValue
                print("Ders başarıyla kaydedildi.")
        except Exception as e:
            print(f"Hata: {e}")

    def find(self, code):
        
        seekSummary = SeekOffsetCalculator.determineSeekValueAndOffset(self.lessonFileIndex, code)
        jumpToSeekValue = seekSummary["jumpToSeekValue"]
        currentLessonOffset = seekSummary["currentRecordOffset"]

        with FileReader.open(self.filePath) as file:
            file.seek(jumpToSeekValue)
            currentLessonLines = file.read(currentLessonOffset)
            print("*** Ders Kaydı ***")
            print(currentLessonLines)
    

    def update(self, code):

        print(self.lessonFileIndex)
        seekSummary = SeekOffsetCalculator.determineSeekValueAndOffset(self.lessonFileIndex, code)
        jumpToSeekValue = seekSummary["jumpToSeekValue"]
        currentLessonOffset = seekSummary["currentRecordOffset"]

        firstPartLines = []
        lastPartLines = []
        with FileReader.open(self.filePath) as file:
            file.seek(0)
            firstPartLines = file.read(jumpToSeekValue).splitlines()
            print(firstPartLines)
            file.seek(currentLessonOffset + jumpToSeekValue)
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
            lesson = LessonRecorder.create()
            lessonSummary = lesson.prepareSummaryAsWritableFormat()
            file.write(lessonSummary)
            newLessonOffSetValue = len(lessonSummary)
            self.lessonFileIndex[lesson.code] = newLessonOffSetValue
            print("Ders başarıyla güncellendi.")
        
        with FileWriter.open(self.filePath) as file:
            content = ""
            for line in lastPartLines:
                content += line + "\n"
            file.writelines(content)