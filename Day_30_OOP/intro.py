# class:
class Maths:
    def __init__(self,name,about):
        self.name=name
        self.about=about
        self.list=[1,2,3,4,5,6]
        
             
    def display(self):
        i=0
        print(f'my name is{self.name} and it is about {self.about}')
        print(self.list[0:3:1])
        while i<10:
            print(i)
            i+=1
        

M=Maths('Peter','student')
M.display()


        