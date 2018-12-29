def person(name ,*data):
    print("name:",name)
    print(data)
person('vikas',12,'vaarnasi',9855283132)
print()
print()

def person(name ,**data):
    print("name:",name)
    print(data)
person(name='vikas',age=12,add='vaarnasi',mob=9855283132)

