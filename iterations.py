#...................Iteration........................
fruit=("apple","mango","grapes")
myItr=iter(fruit)
print(next(myItr))
print(next(myItr))
print(next(myItr))
print()

#...................Iteration of string........................
strng="vikas"
itr=iter(strng)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print()

#...................Iteration of number........................
class myNum():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
num=myNum()
itr=iter(num)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print()

#...................Iteration of number till 20........................
class myNum():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
        
        
num=myNum()
itr=iter(num)

for x in itr:
    print(x)

