#.............File Handling.............
f=open("mydata.txt",'r')

f1=open('abc.txt','w')
f1.write('laptop')
f1=open("abc.txt",'a')

for data in f:
    print(data)


