def helloWorld():
    print("Hello , World")

helloWorld()

#Area of rectangle with parameter
print("Enter the values of length")
l=int(input())
print("Enter the width")
b=int(input())
def areaRect(l,b):
    area=l*b
    print(area)
areaRect(l,b)

#larest two number
print("Enter the first number")
num1=int(input())
print("Enter the second number")
num2=int(input())
def largNum(num1,num2):
    if num1>num2:
        print("num1 is greater")
    elif num2>num1:
        print("num2 is greater")
    else:
        print("bothe are equales")
largNum(num1,num2)
