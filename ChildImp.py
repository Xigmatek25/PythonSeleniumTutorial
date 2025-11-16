from OOPSdemo import Calculator

numChild = 200

class childImp(Calculator):
    def __init__(self):
        Calculator.__init__(self, 10, 20)

    def getCompleteData(self):
        return self.num1 + self.num2 + self.addNumbers()

childObj = childImp()

print(childObj.getCompleteData())