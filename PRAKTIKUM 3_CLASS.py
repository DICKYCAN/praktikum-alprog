'''Basic'''
class Employee:
    count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Employee.count += 1

    def performance_evaluation(self):
        if self.score >= 70:
            print(f"{self.name} has a GOOD performance")
        else:
            print(f"{self.name} has a POOR performance")

andi = Employee('Andi', 85)
rita = Employee('Rita', 60)

andi.performance_evaluation()
rita.performance_evaluation()
print(f'Total Employees: {Employee.count}')

'''Encapsulation'''
class Employee:
    count = 0

    def __init__(self, name, score):
        # instance variable with private access
        self.__name = name
        self.__score = score
        Employee.count += 1

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score

    def updateScore(self, new_score):
        self.__score = new_score

    def performance_evaluation(self):
        if self.__score >= 70:
            print(f"{self.__name} has a GOOD performance with a score of {self.__score}")
        else:
            print(f"{self.__name} has a POOR performance with a score of {self.__score}")

andi = Employee('Andi', 85)
rita = Employee('Rita', 60)

if input("Do you want to update Rita's score? (y/n): ").lower() == 'y':
    new_score = int(input("Enter new score: "))
    rita.updateScore(new_score)

andi.performance_evaluation()
rita.performance_evaluation()
print(f'Total Employees: {Employee.count}')

'''Inheritance'''
class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

class Department(Company):
    def __init__(self, company_name, location, department_name):
        super().__init__(company_name, location)
        self.department_name = department_name

class Employee(Department):
    def __init__(self, company_name, location, department_name, name, score):
        super().__init__(company_name, location, department_name)
        self.__name = name
        self.__score = score

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score

    def updateScore(self, new_score):
        self.__score = new_score

    def performance_evaluation(self):
        return self.__score >= 70

andi = Employee('TechCorp', 'Jakarta', 'IT', 'Andi', 85)
rita = Employee('TechCorp', 'Jakarta', 'HR', 'Rita', 60)

if input("Do you want to update Rita's score? (y/n): ").lower() == 'y':
    new_score = int(input("Enter new score: "))
    rita.updateScore(new_score)

for employee in [andi, rita]:
    status = "GOOD" if employee.performance_evaluation() else "POOR"
    print(f"{employee.getName()} works at {employee.company_name}, department {employee.department_name}, and has a {status} performance with a score of {employee.getScore()}")

'''Polymorphism'''
class Manager:
    def performance_evaluation(self):
        return "Managers have greater responsibility in performance."

class Staff:
    def performance_evaluation(self):
        return "Staff are evaluated based on individual targets."

class Intern:
    def performance_evaluation(self):
        return "Interns are evaluated based on learning ability and adaptation."

employees = [Manager(), Staff(), Intern()]

for e in employees:
    print(e.performance_evaluation())
