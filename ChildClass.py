from Classes import Vehicle


class Jet(Vehicle):

    def __init__(self, wheels, speed, engine, cockpit):
        super().__init__(wheels, speed, engine)
        self.cockpit = cockpit


    def openPit(self):
        print("bzzzzztttt")

jet1 = Jet(3, "mach10", "f22", "Zoids cockpit")

jet1.move()

jet1.openPit()
