#break and continued
for num in range(1,10):
    if num==5:
        break
    else:
        print(num)
print()


#continue
for num in range(1,11):
    if num==5:
        continue
    else:
        print(num)

#...............Book exits or not...............

bookList=["P","C","M"]
print("Enter the book name")
books=input()
for i in bookList:
    if i==books:
        print("I have  book")
        break
else:
    
    print("I dont have book")



        
