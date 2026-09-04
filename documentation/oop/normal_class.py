from abc import ABC , abstractmethod
from dataclasses import dataclass
class Old_person(ABC) : 
    
    
    @abstractmethod
    def big_power(self) :
        pass
        



class person(Old_person) : 
    MIN_AGE = 10
    
    def __init__(self , name , age) :
        self.name = name 
        self.age = age
    
    
    @property
    def display_info(self) : 
        return f"Hello {self.name} , ur age is {self.age}"
    
    @property 
    def age(self) : 
        return self._age 
   
    @age.setter
    def age(self , age) : 
        self._age = age
    @property
    def big_power(self) :
        return "big power" 
    
    
    
    def __str__(self) :
        return f"Person : {self.name} , age : {self.age}"




@dataclass 
class Student : 
    name : str
    age : int
    
    
student = Student('amne', 30)

# print(student)