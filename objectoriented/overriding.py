class Ws:
    def displayA(self):
        print("Hello ")

class Yw(Ws):
    def displayA(self):
        super().displayA()
        print("Welocome Back")


obj = Yw()
obj.displayA()