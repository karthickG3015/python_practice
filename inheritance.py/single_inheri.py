class A:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname)
        print(self.lname)

class B(A):
    def __init__(self,name,fname,lname):
        self.name = name
        super().__init__(fname,lname)

    def display(self):
        # print(self.name)
        # print(self.fname)
        # print(self.lname)
        A.display(self)

obj = B("karthick", "karthick", "Govindaraj")


obj.display()