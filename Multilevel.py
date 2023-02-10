'''
Polymorphism : One namemultiple form.
1. Run time(Method Overiding) : When there is a same method  prototype in your both base class
and derived class, and if you call that method using the object of derived
class then only derived class method will be called. So you can say that
method of derived class overrides the method of base class.
'''

class A:
    def show(self):
        print("Show From A")
class B(A):
    def show(self):
        super().show()
        print("Show From B")
class C(A):
    def show(self):
        super().show()
        print("Show From C")
class D(B,C):
    def show(self):
        super().show()
        print("Show From D")

d1=D()
d1.show()
