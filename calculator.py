#..............CALCULATOR................
import math
def calculator():
    print("Enter the values of a")
    a=float(input())
    print("Enter the vaues of b")
    b=float(input())
    print()
    print("Addition of numbers")
    def adds(a,b):
        add=a+b
        print(add)
    adds(a,b)
    print()
    print("Subtraction of numbers")
    def subs(a,b):
        sub=a-b
        print(sub)
    subs(a,b)
    print()
    print("Multiply of numbers")
    def muls(a,b):
        mul=a*b
        print(mul)
    muls(a,b)
    print()
    print("Divisions of numbers")
    def divs(a,b):
        div=a/b
        print(div)
    divs(a,b)
    print()
    print("Modulas of numbers")
    def mods(a,b):
        mod=a%b
        print(mod)
    mods(a,b)
    print()
    print("Sqrt of the numbers")
    def sqrts(a,b):
        sq=math.sqrt(a)
        sqs=math.sqrt(b)
        print(sq)
        print(sqs)
    sqrts(a,b)
    print()
    print("Powers of numbers")
    def powr(a,b):
        pwr=math.pow(a,b)
        print(pwr)
    powr(a,b)
    
    def powrs(b,a):
        pwrs=math.pow(b,a)
        print(pwrs)
    powrs(a,b)
    print()
    print("floor values of numbers")
    def flr(a,b):
        flrs=math.floor(a)
        flrss=math.floor(b)
        print(flrs)
        print(flrss)
    flr(a,b)
    print()
    print("Ceils values of the numbers")
    def cel(a,b):
        cles=math.ceil(a)
        celss=math.ceil(b)
        print(cles)
        print(celss)
    cel(a,b)
    
calculator()
