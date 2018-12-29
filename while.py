#while loop
temp=77
while temp>=60 and temp<=90:
    print("room temp is maintaines {}".format(temp))
    temp=temp-1

    

#user temp
print("Enter the temp")
temps=int(input())
while temps>=0 and temps<=100:
    print("Room temp is: {}".format(temps))
    temps=temps-1
