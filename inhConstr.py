class A:
    def __init__(self):
        print("in A")

    def f1(self):
        print("hi")

class B(A):
    def f2(self):
        print("hello")

b=B()
print()

#second
class A:
    def __init__(self):
        print("in A")

    def f1(self):
        print("hi")

class B(A):
    def __init__(self):
        super().__init__()
        print("In B")
    def f2(self):
        print("hello")

b=B()
print()

#third
class A:
    def __init__(self):
        print("in A")

    def f1(self):
        print("hi")

class B:
    def f2(self):
        print("hello")
        
class C(B,A):
    def __init__(self):
        super().__init__()
        print("In C")

b=C
()
    


    
