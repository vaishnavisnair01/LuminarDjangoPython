class Parent:
    def phone(self):
        print("i have phone")
class Child(Parent):
    def phone(self):
        print("i have iphone")
c=Child()
c.phone()
