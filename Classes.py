# The concept of classes

class Person:
    def __init__(self, name: str, age: int, gender: str, complexion: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.complexion = complexion
        
    def changeName(self,new_name):
        self.name = new_name
        return "Name changed to {}".format(new_name)
    
    def changeAge(self,new_age):
        self.name = new_age
        return "Age changed to {}".format(new_age)
    
    def changeGender(self,new_gender):
        self.name = new_gender
        return "Gender changed to {}".format(new_gender)
    
    
Kyle = Person("")