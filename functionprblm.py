#function problems
def helloWorld():
    print("Hello World")
helloWorld()

#Sum of two numbers
print("Enter the first num")
num1=int(input())

print("Enter the second num")
num2=int(input())

def sumOfnum(num1,num2):
    add=num1+num2
    print(add)
sumOfnum(num1,num2)

#types of triangle
print("Enter the side1 of tringle")
s1=int(input())

print("Enter the side2 of tringle")
s2=int(input())

print("Enter the side3 of tringle")
s3=int(input())

def typesOftringle(s1,s2,s3):
    if s1==s2 and s2==s3:
        print("Equilateral triangle")
    elif s1==s2 and s2!=s3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
typesOftringle(s1,s2,s3)

