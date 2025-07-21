# Access Specifiers
# 1.pubilic
# 2.private
# 3.protected

# class outter:
#     def __init__(self):
#         self.i=self.inner()
    
#     class inner:
#         def __init__(self):
#             pass
#         def show(self):
#             print('Hello World')  

# o=outter()
# o.i.show()


# polymorphism

# class Parent:
#     def __init__(self):
#         pass
#     def show(self):
#         print('I am a parent class')
#     def show(self):
#         print('i am a child class')    

#  change in the number of paramenters
# changing the paramneters

# print('Achiveres'+'IT')

# class Duck:
#     def talk(self):
#         print('Duck talks')
#     def walk(self):
#         print('Duck walk')

# class Dog:
#     def talk(self):
#         print('Dog Barks')
#     def walk(self):
#         print('Dog wlaks')    

# def call(pet):
#     pet.talk()
#     pet. walk() 

# call(Dog())  
# call(Duck())


class Animal:
    def show(self):
        print('Animal specks')
class Cat(Animal):
    def show(self):
        print('Cat specks')
class Dog(Cat):
    def show(self):
        print('Dog Barks') 

def call(animal):
    animal.show()

call(Animal())
call(Cat())
call(Dog())


class Parent:
    def show(self):
        print('This is a parent class')
class Child(Parent):
    def show(self):
        print('This is a Child class')

def call(human):
    human.show()

call(Parent())
call(Child()) 

def___add__(self,other)



        