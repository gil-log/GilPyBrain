class Language:
    default_language = "한국어"

    def __init__(self):
        self.show = '나의 언어는 ' + self.default_language

    @classmethod
    def classMyLanguage(self):
        return self()

    @staticmethod
    def staticMyLanguage():
        return Language()

    def printLanguage(self):
        print(self.show)


class secondLanguage(Language):
    default_language = "영어"


staticmethod = secondLanguage.staticMyLanguage()
classmethod = secondLanguage.classMyLanguage()

staticmethod.printLanguage()
classmethod.printLanguage()