import math 
import math as m
print("Select the choices from the given lists:")
print("Enter 1 for additions")
print("Enter 2 for subtractions")
print("Enter 3 for multiplications")
print("Enter 4 for divisions")
print("Enter 5 for modulas")
print()
def calculate():
    
    print()
    print("Enter the values of a")
    a=float(input())
    print("Enter the vaues of b")
    b=float(input())
    ad=int(input())
    print()
    print("Addition of numbers")
    
    def ads(ad):
        def adds(a,b):
            add=a+b
            print(add)
        adds(a,b)
    ads(ad)
    
    sb=int(input())
    print()
    print("Subtraction of numbers")
    def sbs(sb):
        def subs(a,b):
            sub=a-b
            print(sub)
        subs(a,b)
    sbs(sb)
    
    mu=int(input())
    print()
    print("Multiply of numbers")
    def mus(mu):
        def muls(a,b):
            mul=a*b
            print(mul)
        muls(a,b)
    mus(mu)
    
    dv=int(input())
    print()
    print("Divisions of numbers")
    def dvs(dv):
        def divs(a,b):
            div=a/b
            print(div)
        divs(a,b)
    dvs(dv)
    
    md=int(input())
    print()
    print("Modulas of numbers")
    def mds(md):
        def mods(a,b):
            mod=a%b
            print(mod)
        mods(a,b)
    mds(md)
calculate()

    
            
        
            
        
    
