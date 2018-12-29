import array as a
def ace():
    vals = a.array("i", [10, 8, 14, 55, 4])
    print(vals)
    x=list(vals)
    x.sort()
    print(x)
ace()

# factorilas numbers
y=5
fact=1
for j in range(1,y+1): # 1 to 5
    fact=fact*j
    print(fact)




