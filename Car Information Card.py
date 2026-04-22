class Car:
    brand=""
    color=""
    speed=""

    def __init__(self,brand,color,speed):
        self.brand=brand
        self.color=color
        self.speed=speed 
    def CarDetails(self):
        print("Car brand is :",self.brand,"|","Car color is :",self.color,"|","Car speed is :",self.speed,"km/h")
        if self.speed>=150:
            print(self.brand,"Car speed is Fast")
        else:
            print(self.brand,"Car speed is Normal ")

car1=Car("Toyota","White",120)
car2=Car("Yaris","Red",200)
car3=Car("Honda Civic","Grey",140)
car4=Car("Alto","Silver",100)

car1.CarDetails()
car2.CarDetails()
car3.CarDetails()
car4.CarDetails()