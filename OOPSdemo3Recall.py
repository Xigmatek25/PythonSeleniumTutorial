class Calculator:

    num = 100

    def __init__(self, num1, num2, exp1):
        self.num1 = num1
        self.num2 = num2
        self.exp1 = exp1

    def addClassVariable(self):
        return self.num1 + Calculator.num

    def addNumbers(self):
        return self.num1 + self.num2

    def subNumbers(self):
        return self.num1 - self.num2

    def getExponent(self):
        i = 1
        x = self.num1
        while i < self.exp1:
            x = x * self.num1
            i = i+1
        return x

            #1 < 4
            # x = 3 * 3 = 9

            #2 < 4
            #x = 9*3 = 27

            #3 < 4
            #x = 27 * 3 = 81

obj = Calculator(3, 5, 4)

print(obj.addClassVariable())

exObj = Calculator(6, 5, 9)

print(exObj.getExponent())







