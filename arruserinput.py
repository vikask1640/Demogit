import array as a
arr=a.array("i",[])
n=int(input("Enter the length of array"))
for i in range(n):
    x=int(input("enter the next values"))
    arr.append(x)
print(arr)

vals=int(input("search element by index"))
print(arr.index(vals))


