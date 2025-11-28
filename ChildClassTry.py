from OOPSdemo2 import Calculator

class ChildImpl(Calculator):

    num2 = 200

    def __init__(self, num1, num2, num3):
        super().__init__(num1, num2)
        self.num3 = num3

    def mulNumbers(self):
        return self.num1 * self.num2 * self.addNumbers() * self.num3


childObj = ChildImpl(2,10, 3)

print(childObj.mulNumbers())