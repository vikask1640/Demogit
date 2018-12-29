#.............Image File Handling.............
f=open("images.jpg",'rb')

f1=open('mypic.jpg','wb')
for i in f:
    f1.write(i)


