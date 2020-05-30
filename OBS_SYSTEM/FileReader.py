
class FileReader:

    @staticmethod
    def open(filePath, encoding = "UTF-8"):
        file = open(filePath, "r", encoding=encoding)
        return file