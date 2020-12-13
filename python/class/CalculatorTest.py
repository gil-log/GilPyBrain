
import Calculator

calculatorA = Calculator.Calculator(1, 2)

calculatorB = Calculator.Calculator(1, 22)

calculatorC = Calculator.ChildCalculator(1, 22)



print(calculatorA.add())
print(calculatorB.add())

print(calculatorC.add())