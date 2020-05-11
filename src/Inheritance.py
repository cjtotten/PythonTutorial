'''
Created on May 11, 2020

@author: cjtotten
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    #print(self.firstname + " " + self.lastname + " is in the " + str(self.grade) +  "th grade")
     
#Use the Person class to create an object, and then execute the printname method:

#x = Person("John", "Doe")
#x.printname()

class Student(Person):
    '''
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        # OR
    '''
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
x = Student("Jonathan", "Totten", 2020)
#x.printname()
x.welcome()
