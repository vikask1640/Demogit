#neasted loop and print the matrix

#1 2 3
#4 5 6
#7 8 9

num=1
for row in range(1,4):
    for coloumn in range(1,4):
        print(num,end='')
        num=num+1
    print()


#user input
print("Enter the number")
num=int(input())
for row in range(1,4):
    for coloumn in range(1,4):
        print(num,end='')
        num=num+1
    print()
