
class Calculator:
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def setNumber(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def add(self):
        resultNumber = self.firstNumber + self.secondNumber
        return resultNumber

    def multiple(self):
        resultNumber = self.firstNumber * self.secondNumber
        return resultNumber

    def sub(self):
        resultNumber = self.firstNumber - self.secondNumber
        return resultNumber

    def divide(self):
        resultNumber = int(self.firstNumber / self.secondNumber)
        return resultNumber

class ChildCalculator(Calculator):
    def add(self):
        print("Overriding")
        return self.firstNumber, self.secondNumber