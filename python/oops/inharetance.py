class employ:
    company = "ABC Inc."
    def __init__(self):
        print("Hello Employ")
    def show(self):
        print(f"The name of the employ is {self.name} and the designation of the employ is {self.designation}")

class coder:
    lanuage = "javascript"
    def printlanguage (self):
        print(f"The language of the coder is {self.lanuage}")

class programmer(employ, coder):
    company = "ppc inc"
    def __init__(self):
       print("How are you")


a = employ()
b = programmer()
b.show
b.printlanguage()
print(a.company, b.company)