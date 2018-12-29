#...............Exeception handling.................

#No message print

a=5
b=2
try:
    print(a/b)
except Exception:
    print("a divided by b")
print("byee")
print()

#With message when error occur
a=5
b=0
try:
    print(a/b)
except Exception:
    print("a is not divided by b")
print("byee")
print()

#With message 

a=5
b=2
try:
    print("Resources open")
    print(a/b)
except Exception as e:
    print("a divided by b".e)
finally:
    print("Resources closed")
print("byee")
print()
