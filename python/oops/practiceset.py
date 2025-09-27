#Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 
class Programmer:
    company = "Microsoft"
    def __init__(self, name, age, salary, designation,language):
      self.name= name
      self.age= age
      self.salary= salary
      self.designation = designation
      self.language = language


Rohan = Programmer("Rohan",29, 10000,"Software Engineer","Python")
print(Rohan.__dict__)
lizz = Programmer("Lizz", 28, 10000, "Software Engineer", "Python")
print(lizz.__dict__)

#  Write a class “Calculator” capable of finding square, cube and square root of a 
# number.
class Calculator:
    def __init__(self,number):
       self.number = number
    def square (self):
       return self.number ** 2
    def cube (self):
       return self.number ** 3
    def square_Root (self):
       return self.number ** 0.5
num = Calculator(4)
print(num.square_Root()) 


#  Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?
class test:
   a = 9 #this is class attribute

num = test()
num.a = 0 
print(num.a) # prints 0
print(test.a)

# Add a static method in problem 2, to greet the user with hello. 
class greeting:
   @staticmethod
   def greet():
      print("Hello D hepta")

dr = greeting()
greeting.greet() # prints Hello D hepta


# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways

