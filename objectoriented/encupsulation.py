class Student:

    def __init__(self):
        self._name = " "
    def getname(self):
        return self._name

    def setname(self,name):
        self._name = name




obj = Student()
obj.setname("Khimding")
s = obj.getname()
print(s)