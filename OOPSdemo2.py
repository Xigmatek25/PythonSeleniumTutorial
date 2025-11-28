#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose and are called differently

class Calculator:
    num = 100       #class variables

    def __init__(self, num1, num2): #instance variables
        print("I am initialized")
        self.num1 = num1
        self.num2 = num2

    def addNumbers(self):
        return self.num1 + self.num2

    def subNumbers(self):
        return self.num1 - self.num2

    def addNumWithClssVriable(self):
        return self.num1 + self.num2 + Calculator.num    #need to call it via class name


    def getData(self):
        print("I am now executing")

                 
#obj = Calculator()
#obj.getData()
#print(obj.num)
if __name__=="__main__":
    tryObj = Calculator(5, 2)

    print(tryObj.addNumbers())
    print(tryObj.subNumbers())
    print(tryObj.addNumWithClssVriable())
