
class Lesson:

    def __init__(self, code, description):
        self.code = code
        self.description = description
    
    def prepareSummaryAsWritableFormat(self):

        content = ""
        content += self.code + "\n"
        content += self.description + "\n"
        return content