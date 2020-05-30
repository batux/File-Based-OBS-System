
class ChoiceSelector:

    @staticmethod
    def selectOperation():
        
        choice = -1
        try:
            choice = int(input("İşlem tercihiniz:"))
        except Exception as e:
            print(f"Hata: {e}")
        
        return choice