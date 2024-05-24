class ClassA:
    def first_method(self):
        print("Johnny Johnny...")
    def secnod_method(self):
        print("Yes Papa.")
    def third_method(self):
        print("Eating Sugar...")
class ClassB(ClassA):
    def second_method(self):
        super().first_method()
        super().second_method()
        super().third_method()
        print("NO Papa.")
    def third_method(self):
        print("Telling Lies...,")
class ClassC(ClassB):
    def first_method(self):
        print("Open your mouth..., Ha.Ha.Ha")
    def second_method(self):
        print("No Papa.")
    def third_method(self):
        super().second_method()
        super().third_method()
        self.second_method
obj_A=ClassA()
obj_B=ClassB()
obj_C=ClassC()


