import numpy
import sys
print(sys.getrecursionlimit)
def great():
    print("Hello")
    great()
great()

#fact of num
def fact(n):
    return n*fact(n-1)
result=fact(5)
print(result)

