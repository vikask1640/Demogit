#...............Method Overriding.................
class A:
    def show(self):
        print("In A")
class B(A):
    def show(self):
        print("In B")
    
b1=B()
b1.show()
