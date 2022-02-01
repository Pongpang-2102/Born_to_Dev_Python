class Vehicle:
    licenseCode = ""
    SerialCode = ""
    def turnOnAirCondtioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    def SayHello(self):
        print("Hello World")

class PickUp(Vehicle):
    Color=""
    def addtoPickupDB(self):
        print("Added Vehicle:PickUp's Color as:", self.Color)

class Van(Vehicle):
    CapPassenger=""
    def addtoVanDB(self):
        print("Added Vehicle:van's cap as:", self.CapPassenger)
class EstateCar(Vehicle):
    pass;


#PickUp1=PickUp()
#PickUp1.turnOnAirCondtioner()

Car1=Car()
Car1.turnOnAirCondtioner()
Car1.SayHello()

PickUp1=PickUp()
PickUp1.turnOnAirCondtioner()
PickUp1.Color="Red"
PickUp1.addtoPickupDB()

Van1=Van()
Van1.turnOnAirCondtioner()
Van1.CapPassenger=15
Van1.addtoVanDB()


EstateCar1=EstateCar()
EstateCar1.turnOnAirCondtioner()




