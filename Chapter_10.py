class Car:
    
    def __init__(self):
        self._year_model = input("What is the car year and model? ")
        self._make = input("What is the make of the car? ")
        self._speed = 0

    
    def accelerate(self):
        self._speed += 5

    def brake(self):
        self._speed -= 5


    def get_speed(self):
        return self._speed

def main():

  

    #create car object
    user_car = Car()
    #call accelerate 5 times
    for i in range(5):
        user_car.accelerate()  
        print("The current speed is", user_car.get_speed())
    #call brake 5 times
    for i in range(5):
        user_car.brake()
        print("The current speed is", user_car.get_speed())

main()

    