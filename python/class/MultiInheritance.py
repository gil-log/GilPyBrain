# 다중 상속

class Human:
    def talk(self):
        print("말을 한다.")
    def eat(self):
        print("overriding없이 먹는다.")

class Developer:
    def coding(self):
        print("coding 한다.")

class Gillog(Human, Developer):
    def talk(self):
        print("gillog는 overriding 하여 말을 한다")
    def coding(self):
        print("gillog는 overriding 하여 코딩 한다")
