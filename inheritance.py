#single level
print("Single Level")
class A:
    
    def f1(self):
        print("hi")

    def f2(self):
        print("hello")

class B(A):
    
    def f3(self):
        print("vikas")

    def f4(self):
        print("sachin")

a1=A()
a1.f1()
a1.f2()

b1=B()
b1.f3()
b1.f4()
print()
print("multi level")
#multi level
class A:
    
    def f1(self):
        print("hi")

    def f2(self):
        print("hello")

class B(A):
    
    def f3(self):
        print("vikas")

    def f4(self):
        print("sachin")

class C(B):
    
    def f5(self):
        print("Lucky")


a1=A()


b1=B()
b1.f1()
b1.f2()

c1=C()
c1.f3()
c1.f4()
c1.f5()
print()
print("Multiple Level")
#multiple level
class A:
    
    def f1(self):
        print("hi")

    def f2(self):
        print("hello")

class B:
    
    def f3(self):
        print("vikas")

    def f4(self):
        print("sachin")


class C(B,A):
    
    def f5(self):
        print("Lucky")

c1=C()
c1.f1()
c1.f2()
c1.f3()
c1.f4()
c1.f5()


        



        
