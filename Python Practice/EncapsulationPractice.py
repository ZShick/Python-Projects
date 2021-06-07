class Protect:
    #creating a class
    def __init__(self):
        #initializing the class and giving it both protected and private variables by using private and protected attributes
        self._protectedVar = 0
        self.__privateVar = 13

    #creating a function within the class that prints one of the variables value
    def getPriv(self):
        print(self.__privateVar)
#creating a function that allows one to change the private variable value
    def setPriv(self, private):
        self.__privateVar = private

#showing my work by calling on functions that print the private and protected variables value, alter the value of the private one, then print the new value.
obj = Protect()
obj.getPriv()
obj.setPriv(100)
obj._protectedVar = 7
obj.getPriv()
print(obj._protectedVar)
