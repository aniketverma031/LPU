# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number:"))

# try:
#     d=a//b
#     print(d)
#     print("valid try")
# except ZeroDivisionError:##during runtime the program will not be terminated the problem will be h
#     print("Division by zero is not allowed")








# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number:"))

# try:
#     d=a//b
#     print(d)
#     print("valid try")
# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# else:
#     print("else")

# finally:#to break the connection
#     print("Inside finally")








# a=10
# b=0

# try:
#     d=a//g
#     print(d)
#     print("valid try")
# except (ZeroDivisionError,NameError) as obj:
#     print(obj)




# class TooYoungException(Exception):
#     def __init__(self,args):
#         self.msg = args

# class TooOldException(Exception):
#     def __init__(self,args):
#         self.msg = args


# age =int(input("enter your age:"))
# if age>18 and age<60:
#     raise TooYoungException("Plz wait some more time you will get married.")
# if age>60 :
#     raise TooOldException("Your age already crossed for marriage")

# else:
#     print("you will get match detail soon by small!!")







class TooYoungException(Exception):
    def __init__(self, args):
        self.msg = args
    def __str__(self):
        return self.msg

class TooOldException(Exception):
    def __init__(self, args):
        self.msg = args
    def __str__(self):
        return self.msg

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise TooYoungException("Plz wait some more time, you will get married.")
    elif age > 60:
        raise TooOldException("Your age already crossed for marriage.")
    else:
        print("You will get match details soon!")
except TooYoungException as e:
    print("TooYoungException:", e)
except TooOldException as e:
    print("TooOldException:", e)
