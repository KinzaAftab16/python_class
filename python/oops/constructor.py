class dev:
    desingnation="Senior"
    language = "Javascript" #This is class attribute 
    def __init__(self, name , salary, designation, language): #This is dunder method which qutomatically called
        self.name  = name
        self.salary = salary
        self.desingnation = designation
        self.language = language
        print("I am developer")


robin = dev("robin rebonson" , 300000, "senior developer", "Java")
print(robin.name, robin.salary, robin.desingnation, robin.language)
print(robin)