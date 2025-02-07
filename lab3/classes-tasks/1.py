class AAA:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input()

    def printString(self):
        print(self.text.upper())


obj = AAA()
obj.getString()
obj.printString()
