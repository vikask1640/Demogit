class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()
        
    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class Laptop:#inner class
        
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=6

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student('vikas',23)
s2=student('akash',26)

s1.show()
                
