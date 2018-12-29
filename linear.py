#..........Linear search..........
pos=0
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
list=[4,15,3,8,5]
n=1
if search(list,n):
    print(n,"Found at",pos,"locations")
else:
    print("Not found")
