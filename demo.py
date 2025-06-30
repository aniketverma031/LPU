# class Test(object):
#     def __init__(self):#constructor :if i have to write only one logic write it in constructor (one time execution logic) else in methods.
#         print("i am from constructor")
#     def m1(self):
#         print("Hello world")
# x = Test()
# x.m1()






# class Bank(object):
#     def __init__(self,name):
#         print("Bank management:")
#         name=input("enter name:")
#         name = self.name
#         print(name)
#     def withdraw(self):
#         print("withdraw")

#     def deposite(self):
#         print("deposite")

#     def statement(self):
#         print("Statementr")
    
#     def mini_statement(self):
#         print("mini statement")


# x=Bank()
# x=Bank(aniket)
# x.withdraw()
# x.deposite()
# x.statement()
# x.mini_statement()




########################Inheritence : child class inheriting the properties of parent class  ###############################
# class Father:
#     def show(self):
#         print("father class inheritence Method")
    
# class Son(Father):
#     def disp(self):
#         print("Son class inheritence Method")

# S=Son()
# S.show()
# S.disp()




#############################################  multi level inheritence   ##########################################
# class Grandfather:
#     def view(self):
#         print("grandfather class inheritence method")
# class Father(Grandfather):
#     def show(self):
#         print("father class inheritence Method")
    
# class Son(Father):
#     def disp(self):
#         print("Son class inheritence Method")

# S=Son()
# S.view()
# S.show()
# S.disp()




######################################## multiple Inheritence ##############################################
# class mother:
#     def view(self):
#         print("Mother class inheritence Method")
# class Father:
#     def show(self):
#         print("father class inheritence Method")
    
# class Son(Father,mother):
#     def disp(self):
#         print("Son class inheritence Method")

# S=Son()
# S.view()
# S.show()
# S.disp()





######################################### Abstractor ######################################################
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
# d = Dog()
# d.speak()  

# c = Cat()
# c.speak()  





