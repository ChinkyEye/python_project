class AClass:
    def displayA(self):
        print("Welcome to displayA")

class BClass(AClass):
    def displayB(self):
        print("Welcome to displayB")

class CClass:
    def displayC(self):
        print("Welcme to C")

class DClass(AClass,CClass):
    def displayD(self):
        print("Welcme to D")

objB = BClass()
objB.displayA()
objB.displayB()

objD = DClass()
objD.displayA()
objD.displayC()