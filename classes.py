class Receptionist:
    def __init__(self, name, gender, age, stack):
        self.name = name
        self.gender = gender
        self.age = age
        self.stack = stack
        
    def __str__(self):
        return f" Name = {self.name} \n Gender = {self.gender} \n Age = {self.age} \n Stack = {self.stack}"
    
    def called(self):
        return f" Yes! \n I am {self.name}, how may I be of help?"
    
    def buy(self, items):
        item = ", ".join(items)     
        return f" I bought {item} \n Here is your change, sir!"
    
items = ["apple", "oranges", "banana", "plantain"]

Receptionist1 = Receptionist("Anthony", "male", 34, "frontend")

print(Receptionist1.buy(items))