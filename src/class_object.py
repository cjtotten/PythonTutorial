'''
Created on May 11, 2020

@author: cjtotten
'''
class Person:
    
    def __init__(self, name, age):        
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is " + self.name  + " and I am " + str(self.age) + " years old")

p1 = Person("Clinton", 44)
p1.myfunc()
