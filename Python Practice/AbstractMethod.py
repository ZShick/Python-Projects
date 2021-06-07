from abc import ABC, abstractmethod
#importing the necessary module
class spaceship(ABC):
    def lightyears(self, amount):
        print("Distance to destination: ", amount)
#creating a class and a couple of functions with it
    def distancePurcahsed(self, amount):
        pass
    #passing the burden of defining this function on to the next class

class lightYearsPurchased(spaceship):
#Here is where the implementation of the distancedPurchased function is defined
    def distancePurchased(self, amount):
        print('The distance to your destination of {} exceeds the amount of lightyears you payed for.'.format(amount))

        #the following whould print out our string telling the user that the destination planet they picked is too far and that they have not purcahsed enought lightyears to get there
obj = lightYearsPurchased()
obj.lightyears("7,999")
obj.distancePurchased("7,999")
