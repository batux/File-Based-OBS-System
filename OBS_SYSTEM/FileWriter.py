
class FileWriter:

    @staticmethod
    def open(filePath, encoding = "UTF-8"):
        file = open(filePath, "a", encoding=encoding)
        return file

    @staticmethod
    def update(filePath, encoding="UTF-8"):
        file = open(filePath, "r+", encoding=encoding)
        return file

    @staticmethod
    def reset(filePath, encoding="UTF-8"):
        file = open(filePath, "w", encoding=encoding)
        return file