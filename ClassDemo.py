class Student:

    def getData(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def putData(self):
        print("First Name : ",self.fname)
        print("Last Name : ",self.lname)

s1=Student()
s2=Student()
s1.getData("Jigar","Thakkar")
s1.putData()
