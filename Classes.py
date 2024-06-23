# The concept of classes

class Person:
    def __init__(self, name, age, gender, complexion):
        self.name = name
        self.age = age
        self.gender = gender
        self.complexion = complexion
        
    def changeName(self,new_name):
        self.name = new_name
        return "Name changed to {}".format(new_name)