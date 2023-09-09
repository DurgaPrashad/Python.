AIM: Write a python script to implement inheritance 
Algorithm:
# Create an object of the child class 
obj = ChildClass("value1", "value2", "value3") 
# Access inherited attributes from the parent class 
print(obj.attribute1) 
print(obj.attribute2) 
# Access attributes specific to the child class 
print(obj.attribute3) 
# Call inherited method from the parent class 
obj.parent_method() 
# Call method specific to the child class 
obj.child_method() 
Source code: 
class Animal(object): 
'''This is the Animal class''' 
def speak(self): 
print('Animals Speak') 
# create a class Dog which inherits the class Animal 
class Dog(Animal): 
'''This the Dog class inherits the Animal class''' 
def bark(self): 
print('Dog barks') 
# class for Puppy which inherits the class Dog class Puppy(Dog): 
'''This is the class Puppy and it inherits the class Dog''' def eats(self):
print('Puppy likes to eat Dog Biscuit')
