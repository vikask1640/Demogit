class computer:

    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu

    def config(self):
        print("Arjun pagal hai:",self.ram,self.cpu)

com1 = computer('i3',12)
com2 = computer('i5',20)

com1.config()
com2.config()
