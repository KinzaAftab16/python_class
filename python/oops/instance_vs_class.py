class Developer:
    name = "Frontend Developer" #This is class attribute
    salary = 30000
    language = "Javascript"

Robin = Developer()
Robin.name = "Robin" # THis is instance attribute
print(Robin.name, Robin.language, Robin.salary)