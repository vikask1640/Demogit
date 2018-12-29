from functools import reduce
from math import sqrt
#lambda a*a
f=lambda a:a*a
result=sqrt(f(5))
print(result)

#lambda a+b
f=lambda a,b:a+b
result=f(5,4)
print(result)

#lambda filter(funct,iterations)
nums=[1,2,5,3,45,156,30]
even=list(filter(lambda n:n%2==0,nums))
print(even)

#lambda map(funct,iterations)
nums=[1,2,5,3,45,156,30]
even=list(filter(lambda n:n%2==0,nums))
double=list(map(lambda n:n*2,even))
print(double)

#lambda reduce(funct,iterations)
nums=[1,2,5,3,45,156,30]
even=list(filter(lambda n:n%2==0,nums))
double=list(map(lambda n:n*2,even))
print(double)
sums=reduce(lambda a,b:a+b,double)
print(sums)

