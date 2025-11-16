class Calculator:
    num = 100 #class variables -> will always be constant

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getData(self):
        print("I am now executing as method in class")

    def addNumbers(self):
        return  self.num1 + self.num2

#obj = Calculator()

#obj.getData()
#print(obj.num)
if __name__=="__main__":

    calc = Calculator(2, 3)

    print(calc.num)

    print(calc.addNumbers())