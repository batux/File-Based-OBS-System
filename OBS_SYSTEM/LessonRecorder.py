from Lesson import Lesson

class LessonRecorder:

    @staticmethod
    def create():
        
        lesson = None
        try:
            code = input("Dersin kısa kodu: ").strip()
            description = input("Ders açıklaması: ").strip()
            lesson = Lesson(code, description)

        except Exception as e:
            print(f"Hata: {e}")

        return lesson

    @staticmethod
    def find():

        code = None
        try:
            code = input("Ders kısa kodu: ").strip()
        except Exception as e:
            print(f"Hata: {e}")
        
        return code