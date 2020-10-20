class Parent:
    def m1(self):
        print("insed parent")
class Child(Parent):
    def m2(self):
        print("inside child")
class Subchild(Child):
    print()