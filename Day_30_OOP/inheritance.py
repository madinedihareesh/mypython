# class parent:
#     def __init__(self):
#         pass

#     def show(self):
#         print('This is a parent class')


# class Child(parent):
#     def __init__(self):
#         pass
#     def display(self):
#         print('This is a child class')

# c=Child()
# c.display()
# c.show()

# # multiple inheritances
# class Father:
#     def __init__(self):
#         pass
#     def king(self):
#         print('Father is the king of the house')


# class Mother:
#     def __init__(self):
#         pass
#     def Queen(self):
#         print('Mother is the queen of the house')

# class son(Father,Mother):
#     def __init__(self):
#         pass
#     def prince(self):
#         print('son is the price of the house')       

# s=son()
# s.prince()
# s.king()   
# s.Queen()


# multilevel:
# class GrandParent:
#     def __init__(self):
#         pass
#     def display(self):
#         print('This is a grand parent class')

# class Parent(GrandParent):
#     def __init__(self):
#         pass
#     def display1(self):
#         print('THis is a parent class')

# class child(Parent):
#     def __init__(self):
#         pass
#     def display2(self):
#         print('This is a child class') 

# c=child()
# c.display2()
# c.display1()
# c.display()

# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         print(f'the area of a rectangle is: {self.l*self.b}')
#     def parimeter(self):
#         print(f'the parimeter of the rectangle is :{(self.l+self.b)*2}')  

# class cuboid(Rectangle):
#     def __init__(self, l, b,h):
#         self.h=h
#         super().__init__(l, b)
#     def vol(self):
#         print(f'the volume of cuboid is:{2*(self.l*self.b*self.h)}')    

# c=cuboid(20,10,30)
# c.area()
# c.parimeter()
# c.vol()


from abc import ABC, abstractmethod

class Parent(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def display(self):
        print('this is a parent class')

class child(Parent):
    def __init__(self):
        pass
    def show(self):
        print(' this is a child class')

c=child()
c.show()
c.display()