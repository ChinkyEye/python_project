class DemoClass:
    a = 10

    def sumData(self):
        print(10+20)

    def addData(self,x):
        self.c = self.a+x
        print(self.c)


demoobject = DemoClass()
print(demoobject.a)
demoobject.sumData()
demoobject.addData(15)
