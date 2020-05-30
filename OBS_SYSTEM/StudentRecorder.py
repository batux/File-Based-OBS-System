from Student import Student

class StudentRecorder:

    @staticmethod
    def create():
        
        student = None
        try:
            no = int(input("Öğrenci numarası: ").strip())
            name = input("Öğrenci ismi: ").strip()
            surname = input("Öğrenci soyismi: ").strip()
            department = input("Öğrenci bölümü: ").strip()
            age = int(input("Öğrenci yaşı: ").strip())

            student = Student(no, name, surname, department, age)

        except Exception as e:
            print(f"Hata: {e}")

        return student

    @staticmethod
    def find():

        no = -1
        try:
            no = int(input("Öğrenci numarası: ").strip())
        except Exception as e:
            print(f"Hata: {e}")
        
        return no