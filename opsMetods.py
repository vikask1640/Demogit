class student:
    school="lpu" #class method

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def schhol(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("student details")
s1=student(33,22,36)
s2=student(40,22,65)

print(s1.avg())
print(s2.avg())

print(student.schhol())

student.info()
        
