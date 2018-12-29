#...............PolyMorphism.................Duck Type

class Poly:
    def execute(self):
        print("Compiling")
        print("Running")
        
class Laptop:
    def code(self,ide):
        ide.execute()

ide=Poly()
lap1=Laptop()
lap1.code(ide)
