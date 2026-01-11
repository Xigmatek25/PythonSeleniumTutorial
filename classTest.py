"""class BasicCalculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


obj = BasicCalculator(10, 5)

print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div()) """


"""class BasicCalculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getData(self):
        print("The system is now getting the data")

obj = BasicCalculator(10, 5)

obj.getData()

with open('test.txt', 'r') as reader:

    lines = reader.readlines()"""

""""
class BasicCalculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addNum(self):
        return self.num1 + self.num2

obj = BasicCalculator(10, 5)

print(obj.addNum())"""


with open('test.txt', 'r') as reader:
    #print(reader.readline())

    lines = reader.readlines()

    for line in lines:
        print(line)

  