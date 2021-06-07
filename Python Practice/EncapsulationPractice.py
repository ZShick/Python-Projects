class Protect:
    def __init__(self):
        self._protectedVar = 0
        self.__privateVar = 13

    def getPriv(self):
        print(self.__privateVar)

    def setPriv(self, private):
        self.__privateVar = private

obj = Protect()
obj.getPriv()
obj.setPriv(100)
obj._protectedVar = 7
obj.getPriv()
print(obj._protectedVar)
