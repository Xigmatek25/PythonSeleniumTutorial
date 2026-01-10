class Vehicle:

    def __init__(self, wheels, speed, engine):
        self.wheels = wheels
        self.speed = speed
        self.engine = engine

    def move(self):
        print("This vehicle is moving at" + self.speed + "km/h")
        print("The engine of this vehicle is" + self.engine)

    