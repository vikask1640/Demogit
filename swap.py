Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #swaping of two num
>>> a=20
>>> b=4
>>> temp=a
>>> a=b
>>> b=temp
>>> print(temp)
20
>>> print(a)
4
>>> print(b)
20
>>> #2nd ways
>>> a,b=b,a
>>> print(a)
20
>>> b,a=a,b
>>> print(b)
20
>>> #3rd ways
>>> a=a^b
>>> b=a^b
>>> a=a^b
>>> print(a)
20
>>> #4th wys
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print(a)
4
>>> print(b)
20
>>> 
